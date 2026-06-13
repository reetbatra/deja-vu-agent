from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import re, json

app = FastAPI()

ROOT = Path('/Users/reet/Developer/deja-vu-agent')
DOCS = ROOT / 'docs'
SKILLS = ROOT / 'skills'

templates = Jinja2Templates(directory=str(ROOT / 'templates'))

def read_texts(folder, pattern):
    out = {}
    for p in folder.glob(pattern):
        out[p.stem] = p.read_text(errors='ignore')
    return out

def match_skill(q, skills):
    text = q.lower()
    for name, body in skills.items():
        tokens = re.findall(r"[a-z0-9_]{3,}", body.lower())[:12]
        if any(t in text for t in tokens):
            return name, body
    return None, None

def save_skill(question, answer):
    slug = re.sub(r'[^a-z0-9]+', '-', question.lower()).strip('-')[:40]
    fname = f"skill-{slug}.md"
    path = SKILLS / fname
    path.write_text(f"# {question}\n\n{answer}\n\nSource: docs/\n")
    return fname

@app.get('/', response_class=HTMLResponse)
async def chat(request: Request):
    docs = read_texts(DOCS, '*.md')
    skills = read_texts(SKILLS, 'skill-*.md')
    return templates.TemplateResponse('index.html', {"request": request, "docs": docs, "skills": skills})

@app.post('/api/chat')
async def chat_api(payload: dict):
    q = (payload.get('message') or '').strip()
    if not q:
        return JSONResponse({"reply": "Send a technical question."})
    docs = read_texts(DOCS, '*.md')
    skills = read_texts(SKILLS, 'skill-*.md')
    name, body = match_skill(q, skills)
    if name:
        return JSONResponse({"reply": f"Seen this before 👀\n\n{body}"})
    answer = "I don't have that yet. Marking this as a new skill."
    fname = save_skill(q, answer)
    return JSONResponse({"reply": f"📝 New skill saved: {fname}\n\n{answer}"})
