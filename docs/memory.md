# Memory System

Hermes has built-in persistent memory that survives across sessions. It stores user facts, preferences, environment details, and lessons learned in a SQLite-backed store.

## Configuration

Memory is enabled in config.yaml:

    memory:
      memory_enabled: true

Persistent memory providers include the built-in backend, Honcho, Mem0, and others. Set the provider via:

    hermes memory setup

## Usage Facts

- Memory is injected into every new conversation turn automatically.
- The agent saves durable facts with the `memory` tool.
- Facts that will be stale in a week should not be saved.
- Do not save task progress, PR numbers, or temporary TODOs.
- Imperative phrasing should be avoided — save declarative facts instead.

## Best Practices

Save user preferences, environment quirks, coding conventions, and recurring fixes. Skip ephemeral task state. When in doubt: will this matter next week? If yes, save it.
