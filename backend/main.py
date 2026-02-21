from fastapi import FastAPI, Request
from backend.github_webhook import handle_github_event

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    return handle_github_event(payload)

@app.get("/")
def health():
    return {"status": "Repo-Scribe alive"}