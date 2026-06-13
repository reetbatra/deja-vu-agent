#!/usr/bin/env python3
import os, re, json, time, pathlib, urllib.request, urllib.error, urllib.parse

ROOT = pathlib.Path('/Users/reet/Developer/deja-vu-agent')
DOCS = ROOT / 'docs'
SKILLS = ROOT / 'skills'
BOT_TOKEN = "8644740064:AAFAmOpwbCLM_3KRapTJXxkPI_6Zwa6XavU"
API = f"https://api.telegram.org/bot{BOT_TOKEN}"
OFFSET_FILE = ROOT / '.offset'

def api(method, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{API}/{method}", data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception as e:
        return None

def send(chat_id, text, parse_mode=None):
    payload = {'chat_id': chat_id, 'text': text}
    if parse_mode:
        payload['parse_mode'] = parse_mode
    return api('sendMessage', payload)

def read_docs():
    out = {}
    for p in DOCS.glob('*.md'):
        out[p.stem] = p.read_text(errors='ignore')
    return out

def read_skills():
    out = {}
    for p in SKILLS.glob('skill-*.md'):
        out[p.stem] = p.read_text(errors='ignore')
    return out

def match_skill(text, skills):
    q = text.lower()
    for name, body in skills.items():
        for token in re.findall(r"[a-z0-9_]{3,}", body.lower())[:10]:
            if token in q:
                return name, body
    return None, None

CONFIRMATIONS = ["noted ✅", "learned ✅"]

def save_skill(question, answer):
    slug = re.sub(r'[^a-z0-9]+', '-', question.lower()).strip('-')[:40]
    fname = f"skill-{slug}.md"
    path = SKILLS / fname
    path.write_text(f"# {question}\n\n{answer}\n\nSource: docs/\n")
    return fname

def main():
    docs = read_docs()
    skills = read_skills()
    offset = 0
    if OFFSET_FILE.exists():
        try: offset = int(OFFSET_FILE.read_text().strip() or 0)
        except: offset = 0
    print('Standalone Telegram support bot running...')
    while True:
        res = api('getUpdates', {'timeout': 30, 'offset': offset + 1, 'allowed_updates': ['message']})
        if not res or not res.get('ok'):
            time.sleep(1)
            continue
        for upd in res['result']:
            offset = max(offset, upd['update_id'])
            msg = upd.get('message') or {}
            chat = msg.get('chat') or {}
            chat_id = chat.get('id')
            text = (msg.get('text') or '').strip()
            if not chat_id or not text:
                continue
            name, body = match_skill(text, skills)
            if name:
                send(chat_id, f"Seen this before 👀\n\n{body}")
            else:
                answer = "I don't have that yet. I'll create a skill for it."
                if docs:
                    first = next(iter(docs.values()))
                    answer = "Check the docs folder for setup details, or I can create a skill from the next answer."
                fname = save_skill(text, answer)
                send(chat_id, f"📝 New skill saved: {fname}")
            OFFSET_FILE.write_text(str(offset))

if __name__ == '__main__':
    main()
