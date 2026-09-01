# wuu web scraper para undertale 

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datetime
import random
import re
from urllib.error import HTTPError, URLError


url = "https://deltarune.wiki/"

try:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/139.0.0.0 Safari/537.36"
        }
    )

    html = urlopen(req)
    bs = BeautifulSoup(html.read(), "html.parser")

    print(bs.h1)

except HTTPError as e:
    print("HTTP Error:", e.code)

except URLError as e:
    print("URL Error:", e.reason)

except Exception as e:
    print("Something else went wrong:", e)


"""
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
"""
"""
html2 = urlopen('https://imagine.gsfc.nasa.gov/science/objects/neutron_stars1.html')
bs2 = BeautifulSoup(html2, 'html.parser')
for link in bs2.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
"""

#random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html3 = urlopen('https://imagine.gsfc.nasa.gov{}'.format(articleUrl))
    bs3 = BeautifulSoup(html3, 'htmlparser')
    return bs3.find('div').find_all('a', href = re.compile('^/science/)((?!:).)*$'))

links = getLinks('/science/objects/neutron_stars1.html')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links.getLinks(newArticle)