# Skills

Skills are Hermes's learning system — reusable how-to guides that persist
across sessions. When the agent solves a complex problem, discovers a
workflow, or gets corrected, it can save that knowledge as a skill document.

## Structure

A skill is a MARKDOWN file with YAML frontmatter:

    ---
    name: my-skill
    description: What it does
    ---
    
    # My Skill
    
    Steps and details here.

The frontmatter name and description are used for skill discovery,
filtering, and display in `/skills` and `hermes skills list`.

## Lifecycle

- **Create**: Agent writes a new skill into `~/.hermes/skills/` or a
  project-local skills directory.
- **Load**: Skills are auto-discovered at startup. Use `/skill name` or
  `hermes -s name` to preload specific ones.
- **Update**: Patch a skill when procedures change; the agent picks up
  the new content on next session.
- **Archive/Pin**: The curator can auto-archive stale skills or pin
  important ones so they are never removed.

## Default Behavior

Skills are sorted by recency of last-modified timestamp and loaded into
the system prompt each conversation. On `/reset` the agent re-scans
`~/.hermes/skills/` for changes.

For persistent skill provenance, add `created_by: agent` in frontmatter.
Bundled/hub-installed skills use their own provenance and are not
touched by the curator.
