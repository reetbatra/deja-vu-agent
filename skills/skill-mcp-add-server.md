# How to Add an MCP Server

## Question: How do I add an MCP server to Hermes?

Use `hermes mcp add <name>` with either `--command` for stdio servers or `--url` for HTTP. Example:

    hermes mcp add filesystem --command "npx @modelcontextprotocol/server-filesystem /path"

After adding, run `hermes mcp list` to confirm, and `hermes mcp test <name>` to verify the connection. MCP tools appear in the normal tool registry and respect approval flows and platform enablement. Use `/reload-mcp` to refresh without restarting.

Source: docs/mcp.md
