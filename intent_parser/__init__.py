# Intent parser module

def parse_intent(command):
    """Parse a natural language command into an intent dictionary."""
    command = command.lower()

    if command.startswith("summarize "):
        file_path = command[len("summarize "):].strip().strip('"')
        return {"type": "summarize_file", "data": file_path}
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        return {"type": "open_app", "data": app_name}
    elif "send email" in command:
        return {
            "type": "send_email",
            "data": {"to": "someone@example.com", "message": "Hello"}
        }
    else:
        return {"type": "unknown", "data": None}