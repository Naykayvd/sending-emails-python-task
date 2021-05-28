import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP('smtp.gmail.com', 587)
sender = 'vandiemennahum@gmail.com'
receivers = ['thapelo@lifechoices.co.za', 'naeemahndavis@gmail.com', 'd.e.fledermaus86@gmail.com']

password = input("enter password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ', '.join(receivers)
msg['subject'] = subject
body = "HI ITS A TEST\n"
body = body + "I am testing\n"
body = body + "HOW ARE YOU!!!"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s.starttls()
s.login(sender, password)
s.sendmail(sender, receivers, text)

s.quit()
