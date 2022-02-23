# -*- coding: utf-8 -*-
"""
Demo for web scraping, based on the
Complete-python-bootcamp on udemy.com
We're going to use the Jonas Salk Wikipedia article
for this example
"""

import requests
from bs4 import BeautifulSoup

# Grabbing a title from a webpage
result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

# Use bs4 to parse the html text from the website
soup = BeautifulSoup(result.text, "lxml")

# Grab the title from the website
title = soup.select('title')

# Just get the text from title without <title>
title_str = soup.select('title')[0].getText()

# Now let's grab all the elements in a class, e.g., the ToC

ToC_text = []
for item in soup.select('.toctext'):
    ToC_text.append(item.text)

print("Table of Contents: ")
print(ToC_text)

# Ok, now let's grab an image from the website
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

print(images)

# Now download one of the images
img_link = requests.get("https:" + images[0])
file = open('Jonas_Salk.jpg', 'wb')
file.write(img_link.content)
file.close()
