import hashlib

from conf import configuration
from crawler import crawl, parse
from cache import load, save
import mail
import pdf


def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


def check_page():
    page = crawl(configuration['targetURL'])  # .decode("utf8")
    page_hash = md5(page)
    c = load()
    if not c['hash'] == page_hash:
        print("HASH CHANGED!")
        print(page_hash)
        # TODO Sent mail or whatever
        match = parse(page.decode('utf8'))
        print(match)

        c['hash'] = page_hash
    else:
        print("Boring old same page...")

    save(c)

check_page()
# mail.send(configuration['mail'])
