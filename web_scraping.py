#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Scrapper
@author: David Guthrie
"""
# TODO: Add support for multiple pages
#		Research using robots.txt and sitemap to navigate site

from bs4 import BeautifulSoup as bSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError, ContentTooShortError

# TODO: Update to read target site from a file
targetSite = "http://books.toscrape.com/"

site_html = downloadSite(targetSite)

site_soup = bSoup(site_html, "html.parser")

# TODO: Update so these parameters are read from a file
containers = site_soup.find_all("article",{"class":"product_pod"})


# Connet to site, get site conntent, disconnect
def downloadSite(url):
    print('Downloading:', url)
    try:
		siteConnection = urlopen(url)
        html = siteConnection.read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
	finally:
		siteConnection.close()
    return html

