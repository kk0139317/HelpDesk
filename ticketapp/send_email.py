import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "kundancoder1@gmail.com"
smtp_password = "csjf yybo ynjd lhmi"

def email_sending(subject, message, email_from, recipient_list):
# Email content
    from_email = smtp_user
    to_email = recipient_list
    subject = subject
    # body = "This is a test email sent from a Python script using SMTP."
    body = message
# Setup MIME
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

# Send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(smtp_user, smtp_password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
