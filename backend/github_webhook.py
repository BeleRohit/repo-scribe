import requests

def handle_github_event(payload: dict):
    print("🔥 Webhook received")

    action = payload.get("action")
    print("Action:", action)

    return {"ok": True}