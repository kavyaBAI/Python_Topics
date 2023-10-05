import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body):
    # Create a multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = subject

    for email in recipient_email:
        reci_name = email[0]
        reci_email = email[1]
        message['To'] = reci_email
        text = f"Dear {reci_name},\n\n{body},\n\nthanks,\ncogniquest team"
        message.attach(MIMEText(text, 'plain'))

        # Create SMTP session for sending the mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('congniquest.team@gmail.com', "zvnsiyjgjfuqgxpi")
            server.sendmail(sender_email, reci_email, message.as_string())
            print("Email sent successfully to", reci_email)

send_email('congniquest.team@gmail.com', [('kavya','Kavyaadithi8787@gmail.com'),('durga','durgashree.s@cogniquest.ai')], 'heykavya', "Yes, it will be completed by this week, but I'm getting errors with some subscriptions.\n I will send the errors along with the update.There might be a configuration issue causing the error. \nPlease find below screenshot for your reference.")
