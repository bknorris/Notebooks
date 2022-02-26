# -*- coding: utf-8 -*-
"""
Demo for working with spreadsheets, based on the
Complete-python-bootcamp on udemy.com

"""

# Working with CSVs

import csv

path = 'c:\\Users\\bknorris\\Documents\\Scripts\\Python\\Python_bootcamp\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\'
data = open(path + 'example.csv',mode='r', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data) # convert CSV to Python object

header = data_lines[0]

# This gets all the emails from the CSV
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

# Get names from the CSV
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+' '+line[2])
    
# Write to CSV
file_to_output = open(path + 'to_save_file.csv', mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']]) # Note: list of lists
file_to_output.close()

# Add some more lines
f = open('to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()

