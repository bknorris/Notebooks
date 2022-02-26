# -*- coding: utf-8 -*-
"""
Demo for working with CSVs and PDFs, based on the
Complete-python-bootcamp on udemy.com

This is the exercise portion of the lecture
"""

import csv
import PyPDF2
import re

path = 'c:\\Users\\bknorris\\Documents\\Scripts\\Python\\Python_bootcamp\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\Exercise_Files\\'
data = open(path + 'find_the_link.csv',mode='r', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data) # convert CSV to Python object

# This gets all the emails from the CSV
all_emails = []
for counts, line in enumerate(data_lines[0:]):
    text = line[counts]
    all_emails.append(text)
    
html = ''.join(all_emails)

# Get the phone number from the PDF
f = open(path + 'Find_the_Phone_Number.pdf',mode='rb') # read file
pdf_reader = PyPDF2.PdfFileReader(f) # open as an object

phone_number = []
for page in range(1,17):
    page_text = pdf_reader.getPage(page)
    page_text = page_text.extractText()
    pattern = r'\d{3}[-.]\d{3}[-.]\d{4}'
    reg = re.search(pattern,page_text)
    if not reg:
        continue
    else:
        phone_number = reg.group()

f.close()
print("phone number is: " + phone_number)