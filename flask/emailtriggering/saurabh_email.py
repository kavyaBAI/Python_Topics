import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail_for_password(to_mail_id, new_password):
	mail_content = """
<div style="border:1px black solid;padding-top:10px;   font-family: Arial, sans-serif; color: black;">
Dear user,
<br>
Your password has been reset and the new password is <b>%s</b>
<br>
Please change your password on your login.
<br><br>
Warm Regards,
<br>
CogniQuest
<br><br>
*** This is an automatically generated email, please do not reply to this email *** </div>""" % new_password
	# The mail addresses and password
	sender_address = 'tablextract@cogniquest.ai'
	sender_pass = '1sj02is019$'
	# sender_address = 'cq.authenticate@gmail.com'
	# sender_pass = 'nathan@123'
	receiver_address = to_mail_id
	# Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	# The subject line
	message['Subject'] = 'Your credentials was reset - CogniQuest'
	# The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'html'))
	# Create SMTP session for sending the mail
	# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	#session = smtplib.SMTP('smtp.office365.com', 587)  # use gmail with port
	session = smtplib.SMTP('smtp.office365.com', 465)  # use gmail with port
	session.starttls()  # enable security
	session.login(sender_address, sender_pass)  # login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')


def send_mail(to_mail_id, otp):
	mail_content = """
<div style="border:1px black solid;padding-top:10px;   font-family: Arial, sans-serif; color: black;">
<br>
Use <b>%s</b> as one time password (OTP) to verify your email. Do not share this OTP to anyone for security reasons. Valid for 15 minutes.
<br><br>
Warm Regards,
<br>
CogniQuest
<br><br>
*** This is an automatically generated email, please do not reply to this email *** </div>""" % otp
	# The mail addresses and password
	# sender_address = 'cq.authenticate@gmail.com'
	# sender_pass = 'nathan@123'
	sender_address = 'tablextract@cogniquest.ai'
	sender_pass = '1sj02is019$'
	#receiver_address = 'mails.nathaniel@gmail.com'
	receiver_address = to_mail_id
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Please Verify Your Email Address - CogniQuest'   #The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'html'))
	#Create SMTP session for sending the mail
	#session = smtplib.SMTP('smtp.office365.com', 587) #use gmail with port
	session = smtplib.SMTP('smtp.office365.com', 465) #use gmail with port
	#session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')


if __name__=='__main__':
   send_mail('mails.nathaniel@gmail.com', '1234')
   #send_mail_for_password('mails.nathaniel@gmail.com', '1111')
#_______________________________________________________________________________________________________________________________________________
#another method
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail_for_password(to_mail_id, new_password):
        mail_content = """
<div style="border:1px black solid;padding-top:10px;   font-family: Arial, sans-serif; color: black;">
Dear user,
<br> 
Your password has been reset and the new password is <b>%s</b>
<br>
Please change your password on your login.
<br><br>
Warm Regards,
<br>
CogniQuest
<br><br>
*** This is an automatically generated email, please do not reply to this email *** </div>""" %new_password
	#The mail addresses and password
	#sender_address = 'tablextract@cogniquest.ai'
	#sender_pass = '1sj02is019$'
        sender_address = 'cq.authenticate@gmail.com'
        sender_pass = 'nqxsglfwfbmmhtzp'
	#sender_address = 'cq.authenticate@gmail.com'
	#sender_pass = 'nathan@123'
        receiver_address = to_mail_id
	#Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Your credentials was reset - CogniQuest'   #The subject line
	#The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
	#Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	#session = smtplib.SMTP('smtp.office365.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')


def send_mail(to_mail_id, otp):
        mail_content = """
<div style="border:1px black solid;padding-top:10px;   font-family: Arial, sans-serif; color: black;">
<br> 
Use <b>%s</b> as one time password (OTP) to verify your email. Do not share this OTP to anyone for security reasons. Valid for 15 minutes.
<br><br>
Warm Regards,
<br>
CogniQuest
<br><br>
*** This is an automatically generated email, please do not reply to this email *** </div>""" %otp
	#The mail addresses and password
        sender_address = 'cq.authenticate@gmail.com'
        sender_pass = 'nqxsglfwfbmmhtzp'
	#sender_address = 'tablextract@cogniquest.ai'
	#sender_pass = '1sj02is019$'
	#receiver_address = 'mails.nathaniel@gmail.com'
        receiver_address = to_mail_id
	#Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Please Verify Your Email Address - CogniQuest'   #The subject line
	#The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
	#Create SMTP session for sending the mail
	#session = smtplib.SMTP('smtp.office365.com', 587) #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')


if __name__=='__main__':
   send_mail('mails.nathaniel@gmail.com', '1234')
   #send_mail('nathaniel.n@cogniquest.ai', '1234')
   #send_mail_for_password('mails.nathaniel@gmail.com', '1111')
