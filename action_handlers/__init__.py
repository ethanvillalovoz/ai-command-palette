# Action handlers module

from .open_app import open_app
from .summarize_file import summarize_file
from .send_email import send_email

def handle_action(intent):
    """Dispatch to the appropriate action handler based on intent type."""
    action_type = intent.get("type")
    data = intent.get("data")

    if action_type == "open_app":
        open_app(data)
    elif action_type == "summarize_file":
        summarize_file(data)
    elif action_type == "send_email":
        send_email(data)
    else:
        print(f"Unknown action type: {action_type}")