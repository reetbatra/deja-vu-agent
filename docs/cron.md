# Cron Jobs

Cron provides durable, scheduled agent runs. Jobs survive sessions,
retries on failure, and can deliver results back to Telegram, Discord,
Slack, or email.

## Creating Jobs

    hermes cron create "0 9 * * *" --prompt "Daily briefing"
    hermes cron create "every 2h" --prompt "Check status"

Acceptable schedules:
- Duration: `30m`, `2h`
- Phrase: `every monday 9am`
- Cron: `0 9 * * *`
- ISO: `2026-06-01T09:00:00`

## Per-Job Options

- `--skill skill-name` — attach a skill before the prompt
- `--model provider/model` — override the job's model
- `--script path.sh` — run a script first and inject its output
- `--no-agent` — script IS the job, no LLM
- `--context-from job-id` — chain another job's output in
- `--workdir /path` — run inside a project directory

## Managing Jobs

    hermes cron list            # all jobs
    hermes cron pause/resume ID
    hermes cron edit ID         # change schedule, prompt, delivery
    hermes cron run ID          # trigger immediately
    hermes cron remove ID

Safety rules:
- 3-minute hard run limit per tick
- `.tick.lock` prevents duplicate ticks
- Cron sessions skip memory by default
- `max_iterations` default is 50
