# wuu web scraper para undertale (pikmin ????)

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datetime
import random
import re
from urllib.parse import urljoin
from urllib.error import HTTPError, URLError


url = "https://deltarune.wiki/"

def getLinks(aUrl):
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
    return bs.find('div').find_all('a')

links = getLinks(url)

while len(links) > 0:
        link = links[random.randint(0, len(links) - 1)]
        newArticle = urljoin(url, link.attrs['href'])

        print(newArticle)

        url = newArticle
        links = getLinks(url)






"""
try:
    

    
    def getLinks(aUrl):
        
        

    
    


    print(bs.h1)

except HTTPError as e:
    print("HTTP Error:", e.code)

except URLError as e:
    print("URL Error:", e.reason)

except Exception as e:
    print("Something else went wrong:", e)
"""

"""
def getLinks(articleUrl):
    html = urlopen(url.format(articleUrl))
    bs = BeautifulSoup(html, 'htmlparser')
    return bs.find('div').find_all('a')

links = getLinks('https://deltarune.wiki/')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links.getLinks(newArticle)

"""