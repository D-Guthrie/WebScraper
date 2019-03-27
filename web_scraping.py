#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Web Scrapper
@author: David Guthrie
"""

from bs4 import BeautifulSoup as bSoup
from urllib.request import urlopen

# Site to target for scraping
targetSite = "http://books.toscrape.com/"

# Connet to site, get site conntent, disconnect
siteConnection = urlopen(targetSite)
site_html = siteConnection.read()
siteConnection.close()

site_soup = bSoup(site_html, "html.parser")

# TODO: Add support for multiple pages
#		Research using sitemap to navigate site