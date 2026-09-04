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
characters = []

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

def isCharacter(aUrl, categories):
    
    if not ("Characters" in categories or "Main characters" in categories):
        return False
    split = url.split('/')
    if len(split) <= 0:
        return False
    
    character = split[-1]
    if not(character in characters) and not ("Category" in character):
        return True
    return False


links = getLinks(getSoup(url))

while len(characters) < 10:

        print(f"[{len(characters)}] {url}", end='\t')

        try: 
            soup = getSoup(url)
        except HTTPError:
            url = "https://deltarune.wiki/w/Category:Characters"
            continue

        links = getLinks(soup)
        print(f"({len(links)})")
        categories = getSections(soup)

        if isCharacter(url, categories):
            split = url.split('/')
            character = split[-1]
            characters.append(character)

        if len(links) <= 0:
            url = "https://deltarune.wiki/w/Category:Characters"
        else:
            nextlink = links[random.randint(0, len(links) - 1)]
            url = urljoin(url, nextlink.attrs['href'])

        # time.sleep(0.5)

print("\n\n\nRESULT:")
for l in characters:
    print(l)