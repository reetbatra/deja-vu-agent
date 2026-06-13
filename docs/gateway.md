# Gateway Messaging

The Hermes gateway connects the agent to messaging platforms. It runs as a macOS LaunchAgent in the background and routes messages between the model and the configured platform adapters.

## Platforms

Supported platforms include Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, and more. Each platform has its own adapter under `gateway/platforms/` and is enabled in `config.yaml`.

## Setup

Run the interactive wizard:

    hermes gateway setup

Or directly set the platform flags:

    hermes config set gateway.platforms telegram
    hermes config set gateway.telegram.bot_token <token>

After setup, start the service:

    hermes gateway install

Then control it via:

    hermes gateway start
    hermes gateway stop
    hermes gateway status

## Runtime

The gateway logs to `~/.hermes/logs/gateway.log` and `gateway.error.log`. When running as a LaunchAgent, it survives logouts and reboots. Use `/restart` in-session or `hermes gateway restart` from the CLI to reload config.
