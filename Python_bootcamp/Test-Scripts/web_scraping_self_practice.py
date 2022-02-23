# -*- coding: utf-8 -*-
"""
Demo for web scraping, based on the
Complete-python-bootcamp on udemy.com

In this example, we're doing a self-coding exercise to scrape data from
http://quotes.toscrape.com

The task is to get the names of the author's on the first page,
then get the quotes on the first page, and then the top-10 tags on the first
page. 

The last step is to loop through all the pages on the site and get the unique
authors. 

"""

import requests
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com/page/{}/'
result = requests.get(base_url.format(1))
soup = BeautifulSoup(result.text, 'lxml')

# # Step 1: get unique author names
# unique_authors = set()
# authors = [a.text for a in soup.find_all('small', class_='author')]
# unique_authors.update(authors)

# # Step 2: get matching quotes
# quotes = [q.text for q in soup.find_all('span', class_='text')]

# # Step 3: get top-10 
# soup.select('h2')

# tags = [t.text for t in soup.select('a', class_='tag')]
# last_ten = tags[-10:]  # These are the last ten items on the site

# # Step 4: loop through pages and get unique authors
unique_authors = set()

page = 1
while(True):
    result = requests.get(base_url.format(page))
    soup = BeautifulSoup(result.text, 'lxml')

    if "No quotes found!" in str(soup):
        break
    else:
        print(f'Scraping page number: {page}')
        authors = [a.text for a in soup.find_all('small', class_='author')]
        unique_authors.update(authors)
        page += 1

print(unique_authors)
