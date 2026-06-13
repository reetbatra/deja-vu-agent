# Demo

## FastAPI web demo

1. Start the app
   ```
   python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
   ```
2. Open the UI
   - http://localhost:8080
3. Ask a technical question about docs in `./docs`
4. If it already knows the topic, it'll respond with: `Seen this before 👀`  
   If not, it'll save a new skill file under `./skills` and reply: `📝 New skill saved: skill-...`

## Telegram flow

- Update the bot token in `/Users/reet/.hermes/.env`  
- Enable users with `GATEWAY_ALLOW_ALL_USERS=true`  
- Restart Hermes with `hermes gateway restart`  

## Reuse test

Ask the same question twice. The second reply should come from the saved skill, not a new file.
