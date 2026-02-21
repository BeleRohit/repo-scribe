def handle_github_event(payload: dict):
    # For now, just log what arrived
    event = payload.get("action", "unknown")
    return {
        "message": "Webhook received",
        "action": event
    }