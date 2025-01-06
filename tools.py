from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_email_message(sender: str, email: str, subject: str)-> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText("Default body", "plain"))
    return message
