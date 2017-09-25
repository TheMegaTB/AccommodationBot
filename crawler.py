import urllib.request
import re


def crawl(target, log=True):
    req = urllib.request.urlopen(target)
    print("Crawled ", target)
    if log:
        print("Return code:", req.getcode())
    page = req.read()
    return page


def parse(string):
    matches = [a for a in [re.match(".*\"([^\"]*Antrag[^\"]*docx)\"", line) for line in string.split("\n")] if a is not None]
    for match in matches:
        return match.group(1)
