import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_email(data):
    """Send an email using an SMTP server."""
    try:
        smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
        smtp_port = 587  # Common port for TLS
        sender_email = os.getenv("EMAIL_ADDRESS")  # Use environment variable for email
        sender_password = os.getenv("EMAIL_PASSWORD")  # Use environment variable for password

        print(f"Using EMAIL_ADDRESS: {os.getenv('EMAIL_ADDRESS')}")
        print(f"Using EMAIL_PASSWORD: {os.getenv('EMAIL_PASSWORD')}")

        recipient = data.get("to")
        subject = data.get("subject", "No Subject")  # Default to "No Subject" if not provided
        message_body = data.get("message")

        if not recipient or not message_body:
            raise ValueError("Recipient, subject, and message fields are required.")

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject  # Use the subject from the data
        msg.attach(MIMEText(message_body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())

        print(f"Email sent to {recipient} successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")