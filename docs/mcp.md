# MCP Servers

Model Context Protocol (MCP) servers extend Hermes with external tools.
Hermes includes a built-in MCP client that connects servers via stdio
or HTTP, auto-discovers their tools, and exposes them as first-class
tools in conversations.

## Connecting Servers

**Command-line:**

    hermes mcp add <name> --command "npx server --port 8080"
    hermes mcp add <name> --url http://localhost:8080/mcp

**Interactive:**

    hermes mcp configure <name>   # toggle tool selection
    hermes mcp list               # show configured servers
    hermes mcp test <name>        # verify connection

## Tool Exposure

Once connected, MCP tools appear in the regular tool registry. They
respect Hermes's approval workflows, secret redaction, and platform
enablement (via `hermes tools`).

Use `/reload-mcp` to re-discover tools without restarting.

## Catalog Install

Some MCP servers are available by name:

    hermes mcp install <name>

The client auto-discovers available tools on connection. Each server
publishes a tool manifest; the Hermes MCP layer maps those into the
agent's native tool-calling format.
