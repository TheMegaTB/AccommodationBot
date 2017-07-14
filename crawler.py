import urllib.request
import re


def crawl(target):
    page = urllib.request.urlopen(target).read()
    return page


def parse(string):
    print(type(string))
    print(string)
    match = re.match(".*\"([^\"]*docx)\"", string)
    # match = re.match(r'\"([^\"]*docx)\"', string)
    print(match)
    print(type(match))
    group = match.group(1)
    return group
