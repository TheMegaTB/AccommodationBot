import hashlib
from _thread import start_new_thread
from conf import configuration
from crawler import crawl, parse
from cache import load, save
import mail
import parser


def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def send_smtp_test():
    c = load()
    if not c['smtpTestSent']:
        c['smtpTestSent'] = True
        save(c)
        notification_conf = {
            "body": "This is a test of your smtp settings.\nYour final mail will be sent to " + ", ".join(configuration["mail"]["recipient"]) + ".\n\n- Accommodation Bot",
            "subject": "SMTP Settings Test!",
            "recipient": configuration['mail']['notificationRecipient'],
            "server": configuration['mail']['server']
        }
        mail.send(notification_conf)


def check_page():
    page = crawl(configuration['targetURL'])  # .decode("utf8")
    page_hash = md5(page)
    c = load()
    if not c['hash'] == page_hash:
        print("HASH CHANGED! (" + page_hash + ")")

        # Run a background thread to archive the page in the web archive
        start_new_thread(crawl, ("https://web.archive.org/save/" + configuration['targetURL'], False))

        # Check if the file is online and we didn't sent the mail already (if so send it)
        match = parse(page.decode('utf8'))
        if match is not None and not c['mailSent']:
            print("FILE IS ONLINE! Sending mails ... (and we didn't sent them already)")
            docx = crawl(match)
            for person_details in configuration['details']:
                variables = {
                    "name": person_details['name'],
                    "year": person_details['targetYear'],
                    "quarter": person_details['quarter'],
                    "mail": person_details['mail'],
                    "streetAndCity": person_details['streetAndCity'],
                    "phone": person_details['phone'],
                    "matrikelnr": person_details['matrikelnr']
                }
                res = parser.update_document_contents(docx, person_details)
                res_filename = "Antrag Wohnheimzimmer " + variables['quarter'] + " " + variables['year'] + ".docx"
                mail.send(configuration['mail'], variables, res, res_filename)
            c['mailSent'] = True

        # Send a mail regardless of the above that there is a change
        notification_conf = {
            "body": "Something changed! Go and visit " + configuration['targetURL'],
            "subject": "IMPORTANT | The watched website has changed! Go check it immediately!",
            "recipient": configuration['mail']['notificationRecipient'],
            "server": configuration['mail']['server']
        }
        if c['mailSent']:
            notification_conf['body'] += "\n\n Oh and btw I already sent your reservation request ;)\n\n Have a good one!\n - AccommodationBot"
        mail.send(notification_conf)

        c['hash'] = page_hash
    else:
        print("Boring old same page...")

    save(c)


send_smtp_test()
check_page()
