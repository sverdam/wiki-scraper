# wuu web scraper para undertale (pikmin ????)

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datetime
import random
import re
from urllib.parse import urljoin
from urllib.error import HTTPError, URLError

import time

url = "https://deltarune.wiki/"

def getSoup(aUrl):
    req = Request(
        aUrl,
        headers={
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/139.0.0.0 Safari/537.36"
                
        }
    )

    html = urlopen(req)
    bs = BeautifulSoup(html.read(), "html.parser")
    return bs

def getLinks(aUrl):
    bs = getSoup(aUrl)
    return bs.find('div').find_all('a')

links = getLinks(url)

while len(links) > 0:
        link = links[random.randint(0, len(links) - 1)]
        newArticle = urljoin(url, link.attrs['href'])

        print(newArticle)

        url = newArticle
        links = getLinks(url)
