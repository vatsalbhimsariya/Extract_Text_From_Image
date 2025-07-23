import sendgrid
from sendgrid.helpers.mail import Mail
from config import *

def send_email(subject, body):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=body
    )
    sg.send(email)