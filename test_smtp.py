import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = os.getenv("EMAIL_ADDRESS")
sender_password = os.getenv("EMAIL_PASSWORD")

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        print("SMTP connection successful!")
except Exception as e:
    print(f"SMTP connection failed: {e}")
