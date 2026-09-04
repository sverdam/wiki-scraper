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

def getLinks(bs):
    #bs = getSoup(soup)
    return bs.find('div').find_all('a')

def getSections(bs):
    # bs = getSoup(aUrl)
    categoryDiv = bs.find(class_="utw-page-categories")
    if categoryDiv == None:
        return []
    categoriesListItems = categoryDiv.find_all("li")

    categories = [li.text for li in categoriesListItems]
    # print(categoriesListItems)
    print(categories, end='\n\n')
    return categories

links = getLinks(getSoup(url))

while len(links) > 0:

        print(f"{url}", end='\t')

        soup = getSoup(url)

        links = getLinks(soup)
        print(f"({len(links)})")
        categories = getSections(soup)

        if len(links) <= 0:
            url = "https://deltarune.wiki/w/Category:Characters"
        else:
            nextlink = links[random.randint(0, len(links) - 1)]
            url = urljoin(url, nextlink.attrs['href'])

        time.sleep(0.5)

