# How Cron Scheduling Works

## Question: How does cron scheduling work in Hermes?

Create a job with `hermes cron create "<schedule>" --prompt "<task>"`. Schedules accept durations (`30m`, `2h`), phrases (`every monday 9am`), 5-field cron (`0 9 * * *`), or ISO timestamps. Jobs skip memory by default, have a 3-minute hard limit per tick, and can chain via `--context-from`. Manage them with `hermes cron list`, `hermes cron pause/resume <id>`, and `hermes cron edit <id>`.

Source: docs/cron.md
