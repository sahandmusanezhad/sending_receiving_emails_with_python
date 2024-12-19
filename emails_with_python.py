import smtplib
import getpass
import imaplib

# how to send email with python

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email,password)

from_address = email
to_address = email
subject = input("enter the subject line: ")
message = input("enter the body message: ")
msg = "Subject: {}\n\n{}".format(subject, message)

smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()

# how to receive email with python

M = imaplib.IMAP4_SSL('imap.gmail.com')
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
M.login(email,password)
M.list()
M.select('inbox')
typ, data = M.search(None, 'ON 01-NOV-2024')
email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_maintype() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
