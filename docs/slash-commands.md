# Slash Commands

Hermes supports a rich set of in-session slash commands for control, configuration, and utility. They work in interactive chats and Telegram DMs/groups.

## Session Control

    /new            # fresh session
    /clear          # clear screen + new session (CLI)
    /reset          # alias for /new
    /retry          # resend last message
    /undo           # remove last exchange
    /title <name>   # name the session

## Configuration

    /config         # show config (CLI)
    /model [name]   # show or change model
    /personality [name] # set personality
    /verbose        # cycle verbosity
    /voice [on|off|tts] # voice mode
    /yolo           # toggle approval bypass

## Tools & Skills

    /tools          # manage tools (CLI)
    /skills         # search/install skills (CLI)
    /skill <name>   # load a skill into session
    /reload-skills  # re-scan skills directory
    /curator        # background skill maintenance
    /cron           # manage cron jobs (CLI)

## Gateway

    /approve        # approve pending command
    /deny           # deny pending command
    /restart        # restart gateway
    /sethome        # set current chat as home channel
    /platforms      # show platform connections
    /topic          # Telegram DM topic sessions

## Utility

    /help           # show commands
    /commands       # browse all commands
    /usage          # token usage
    /insights       # usage analytics
    /debug          # upload debug report
    /quit           # exit CLI
