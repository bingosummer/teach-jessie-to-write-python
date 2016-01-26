#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
keyword = sys.argv[2]
r = requests.get(url)
html_doc = r.content
soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all('a'):
    text = link.text
    href = link.get('href')
    if keyword in text:
        print text,
        if href.startswith("http"):
            print href
        else:
            print "http://en.people.cn{0}".format(href)
