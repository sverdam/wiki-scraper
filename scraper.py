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

def getSections(aUrl):
    bs = getSoup(aUrl)
    categoryDiv = bs.find(class_="utw-page-categories")
    if categoryDiv == None:
        return []
    categoriesListItems = categoryDiv.find_all("li")

    categories = [li.text for li in categoriesListItems]
    # print(categoriesListItems)
    print(categories, end='\n\n')

links = getLinks(url)

while len(links) > 0:
        link = links[random.randint(0, len(links) - 1)]
        newArticle = urljoin(url, link.attrs['href'])

        print(newArticle, end='\t')

        url = newArticle
        links = getLinks(url)
        print(f'({len(links)})')

        getSections(newArticle)
        time.sleep(0.5)

