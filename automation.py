import smtplib
import ssl
from email.message import EmailMessage

# Type senders and recievers email
email_sender = 'nitinshukla@gmail.com'
email_password = 'wm**********fjym'
email_receiver = 'xyz@gmail.com'

# Type the subject and body of the mail
subject = 'Just checking in'
body = """
Hey how are you?
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# SSL Layer for security
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
