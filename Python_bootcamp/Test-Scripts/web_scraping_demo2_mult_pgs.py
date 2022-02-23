# -*- coding: utf-8 -*-
"""
Demo for web scraping, based on the
Complete-python-bootcamp on udemy.com

In this example, we will work with multiple pages and items.

We will use a website specifically designed for web scraping:
www.toscrape.com

Goal: get the title of every book with a two-star rating
"""

import requests
from bs4 import BeautifulSoup

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
page_num = list(range(1, 51))  # 50 pages to loop through
titles = []

# Loop through page numbers
for count, page in enumerate(page_num):
    print(f'Scraping page number: {count+1}\n')
    result = requests.get(base_url.format(page))
    soup = BeautifulSoup(result.text, 'lxml')
    products = soup.select('.product_pod')

    # Loop through products on each page
    for id in products:
        if id.select('.star-rating.Two'):
            titles.append(id.select('a')[1]['title'])
        else:
            continue
