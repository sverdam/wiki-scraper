# wuu web scraper para undertale (pikmin ????)

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datetime
import random
import re
from urllib.parse import urljoin
from urllib.error import HTTPError, URLError

import json
import time

from question_generator import generate

url = "https://deltarune.wiki/"
characters = []
data = {}

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

def addCharacter(character, soup:BeautifulSoup):

    def stripBracket(v:str) -> str:
        r = v
        if "[" in v:
            r = v.split('[')[0]
        return r

    print(f"\tV--< {character}")
    tableItems = soup.find_all(class_ = "pi-data")
    tablesData = {}

    for item in tableItems:
        key = item.find(class_ = "pi-data-label")
        value = item.find(class_ = "pi-data-value")
        if key == None or value == None:
            continue

        valueList = value.findAll("li")
        if len(valueList) > 0:
            vals = []
            print(f"\t|--> {key.text}:")
            for li in valueList:
                val = stripBracket(li.text)
                
                print(f"\t.    |--> {val}")
                vals.append(val)
            value = vals
        else:
            val = stripBracket(value.text)
            print(f"\t|--> {key.text}: {val}")
            value = val

        tablesData[key.text] = value
    data[character] = tablesData

    print("\t.")


def saveData():
    jsonString = json.dumps(data, indent=4, sort_keys=True)
    print(jsonString)

    with open("characters.json", "w") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)

links = getLinks(getSoup(url))
jumpsSinceLastSuccess = 0

while len(characters) < 15:

        print(f"[{len(characters)}] {url}", end='\t')
        jumpsSinceLastSuccess += 1

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
            addCharacter(character, soup)
            jumpsSinceLastSuccess = 0

        if len(links) <= 0 or jumpsSinceLastSuccess >= 10:
            url = "https://deltarune.wiki/w/Category:Characters"
            jumpsSinceLastSuccess = 0
        else:
            nextlink = links[random.randint(0, len(links) - 1)]
            url = urljoin(url, nextlink.attrs['href'])

print("\n\n\nRESULT:\n")
for l in characters:
    print(f"- {l}")

print("\nJSON:\n")
saveData()

generate(data)

