#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Web Scrapper
@author: David Guthrie
"""

# TODO: Review and clean up imports
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

# Site to target for scraping
# This should probably be either set in a config file, or input at runtime
targetSite = "http://books.toscrape.com/"

SLEEP_TIME = 1

# look at what is in here
r = requests.get(targetSite)

# look at what is in here
c = r.content

soup = BeautifulSoup(c,"html.parser")
time.sleep(SLEEP_TIME)

# extract first and last page numbers
paging = soup.find("ul",{"class":"pager"}).find_all("li",{"class":"current"})

page_numbers = re.findall('\d+', paging[0].text)

start_page = page_numbers[0]
last_page = page_numbers[1]

# empty list to hold scrapped content
web_content_list = []

for currPage in range(int(start_page),int(last_page)+1):
    
    url = targetSite + "catalogue/page-" + str(currPage) + "/.html"
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    
    product_pod = soup.find_all("article",{"class":"product_pod"})
    
    book_pod_dict = {}
    
    for item_pod in zip(product_pod):
        book_pod_dict["Title"] = item_pod.find("a", {"title"}.text)
        book_pod_dict["Price"] = item_pod.find("p", {"class":"price_color"}.text)
    web_content_list.append(book_pod_dict)
    
df = pd.DataFrame(web_content_list)

df.to_csv("Output.csv")

# TODO: Finish web page downloader function
def download(targetSite):
    print('Downloading:', url)
    try:
        # look at urllib
        html = urllib.request.urlopen(targetSite).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
    return html
