def send_email(data):
    """Mock sending an email by printing the recipient and message."""
    try:
        recipient = data.get("to")
        message = data.get("message")
        if recipient and message:
            print(f"Sending email to {recipient}:\n{message}")
        else:
            print("Invalid email data. 'to' and 'message' fields are required.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")