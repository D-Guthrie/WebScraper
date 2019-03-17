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

r = requests.get(targetSite)
c = r.content

soup = BeautifulSoup(c,"html.parser")

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
def downloader(url, user_agent = '', num_retries = 2, charSet = 'utf-8'):
    print('Downloading from:', url)
    request = urllib.request.Request(url)
