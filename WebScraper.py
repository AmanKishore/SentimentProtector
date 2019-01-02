'''
Web Scraper:
    This file scrapes data from a website.
'''

from lxml import html
import requests
import urllib.request
from bs4 import BeautifulSoup

def scraper(webpage):
    data = urllib.request.Request(webpage)
    html = urllib.request.urlopen(data).read()
    
    # textdat = tree.xpath('//*[@id="rso"]/div[3]/div/div[1]/div/div/div[2]/div/text()')

    return html


print(scraper('https://www.google.com/search?q=facebook&rlz=1C1CHBF_enUS823US824&oq=facebook&aqs=chrome..69i57j69i60j0l4.4870j0j4&sourceid=chrome&ie=UTF-8'))