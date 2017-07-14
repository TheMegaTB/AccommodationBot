import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from time import time


def send(mail_config):
    # Get all configuration values
    recipient = mail_config['recipient']
    subject = mail_config['subject']
    body = mail_config['body']
    server = mail_config['server']

    msg = MIMEMultipart()
    msg['From'] = server['username']
    msg['To'] = COMMASPACE.join(recipient)
    msg['Date'] = formatdate(time() - 60*60*24*2, localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    # for f in files or []:
    #     with open(f, "rb") as fil:
    #         part = MIMEApplication(
    #             fil.read(),
    #             Name=basename(f)
    #         )
    #         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    #         msg.attach(part)

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
    # smtp = smtplib.SMTP(server)
    # smtp.sendmail(server['username'], recipient, msg.as_string())
    # smtp.close()
