#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Web Scrapper
 - from tutorial:
     https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-bc9563fe8860

@author: David Guthrie
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

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



