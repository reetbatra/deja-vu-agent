# How Skills Work

## Question: How do Hermes skills work?

Skills are persistent, reusable how-to guides the agent saves as markdown files in `~/.hermes/skills/`. Each file uses a title, a concise explanation, and source references. On `/reset` or when the agent loads a skill by name, the prior answer is checked first for reuse.

Source files:
- docs/skills.md
- ~/.hermes/skills/autonomous-ai-agents/hermes-agent references
