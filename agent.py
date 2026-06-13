#!/usr/bin/env python3
from pathlib import Path

SKILLS = Path("skills")
DOCS = Path("docs")


def match_skill(question: str):
    q = question.lower()
    for path in sorted(SKILLS.glob("skill-*.md")):
        text = path.read_text(errors="ignore").lower()
        if any(token in q for token in text.split()[:8]):
            return path
    return None


def main():
    print("Deja Vu Agent — ask a technical question about the project in ./docs")
    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not question:
            continue
        hit = match_skill(question)
        if hit:
            print("\nSeen this before 👀")
            print(hit.read_text())
        else:
            print("\nNo saved skill matched this question yet.")
