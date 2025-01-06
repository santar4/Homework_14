from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 2525
smt_server = "smtp.mailmug.net"
login = "ixlvsobhypukdjpg"
password = "qzxnh8qz0fsbrbq6"
sender = "dykovm11@gmail.com"
def create_email_message(sender: str, email: str, subject: str)-> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText("Default body", "plain"))
    return message
