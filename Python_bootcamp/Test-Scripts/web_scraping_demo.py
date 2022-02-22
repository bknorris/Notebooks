# -*- coding: utf-8 -*-
"""
Demo for web scraping, based on the
Complete-python-bootcamp on udemy.com
We're going to use the Jonas Salk Wikipedia article
for this example
"""

import requests
import bs4

# Grabbing a title from a webpage
result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

# Use bs4 to parse the html text from the website
soup = bs4.BeautifulSoup(result.text, "lxml")

title = soup.select('title')
