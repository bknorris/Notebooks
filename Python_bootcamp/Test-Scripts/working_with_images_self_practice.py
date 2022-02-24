# -*- coding: utf-8 -*-
"""
Demo for image processing, based on the
Complete-python-bootcamp on udemy.com

This is the exercise portion of the lecture

The task is to overlap two images to reveal the hidden message!
"""

from PIL import Image

path = 'c:\\Users\\bknorris\\Documents\\Scripts\\Python\\Python_bootcamp\\Complete-Python-3-Bootcamp\\14-Working-with-Images\\'
mask = Image.open(path + 'mask.png')
matrix = Image.open(path + 'word_matrix.png')

mask = mask.resize((1015,559))
matrix.putalpha(128)
mask.paste(im=matrix, box=(0,0),mask=matrix) 
mask.show()

# "Great Work With Images You Are The Best" 