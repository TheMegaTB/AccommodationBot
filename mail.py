import smtplib
import io
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from time import time


def send(mail_config, variables=None, file=None, file_name=None):
    if variables is None:
        variables = {}

    # Get all configuration values
    recipient = mail_config['recipient'].copy()
    subject = mail_config['subject']
    body = mail_config['body']
    server = mail_config['server']

    for mapping in variables:
        body = body.replace("%" + mapping + "%", variables[mapping])
        subject = subject.replace("%" + mapping + "%", variables[mapping])

    msg = MIMEMultipart()
    msg['From'] = server['username']
    msg['To'] = COMMASPACE.join(recipient)
    msg['Date'] = formatdate(time() - 60*60*24*2, localtime=True)
    msg['Subject'] = subject

    if 'mail' in variables:
        msg['CC'] = variables['mail']
        recipient.append(variables['mail'])

    print()
    print("Sending mail to:", recipient)

    msg.attach(MIMEText(body))

    # Add the file to the mail
    if file is not None and file_name is not None:
        f = io.BytesIO(file)
        part = MIMEApplication(f.read(), Name=file_name)
        part['Content-Disposition'] = 'attachment; filename="%s"' % file_name
        msg.attach(part)

    try:
        smtp = smtplib.SMTP(server['hostname'], server['port'])
        smtp.ehlo()
        smtp.starttls()
        smtp.login(server['username'], server['password'])
        smtp.sendmail(server['username'], recipient, msg.as_string())
        smtp.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')
