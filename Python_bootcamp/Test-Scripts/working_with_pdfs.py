# -*- coding: utf-8 -*-
"""
Demo for working with PDFs, based on the
Complete-python-bootcamp on udemy.com

"""

# Working with PDFs
import PyPDF2

path = 'c:\\Users\\bknorris\\Documents\\Scripts\\Python\\Python_bootcamp\\Complete-Python-3-Bootcamp\\15-PDFs-and-Spreadsheets\\'

""" Ok so typically in Python you "open" the file with open() and then
attach a "reader" object to the file. 
"""

f = open(path + 'Working_Business_Proposal.pdf',mode='rb') # read file
pdf_reader = PyPDF2.PdfFileReader(f) # open as an object
page_one = pdf_reader.getPage(1) # get page
page_one_text = page_one.extractText() # view text on page. If empty string, PDF not compatible with PyPDF2

f.close() # Don't forget to do this!

