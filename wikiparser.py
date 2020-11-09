from bs4 import BeautifulSoup
import requests
import urllib.request

from urllib.request import urlopen


def parsewiki(url):
    html = urlopen(url)
    parsed = BeautifulSoup(html, 'html.parser')
    # return parsed.find_all('table')
    imgs = parsed.find_all('img')
    final = ""
    for img in imgs:
        if int(img['width']) > 60 and int(img['height']) > 60:
            final = img
            break

    body_ps = parsed.find("div", id="bodyContent")
    body_ps = body_ps.find_all('p')
    p = body_ps[0].getText()
    return (p, final['src'][2:])
    # return parsed.select('table[class*="infobox"]')


URL = 'https://en.wikipedia.org/wiki/Miami'

print(parsewiki(URL))