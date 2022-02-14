# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:41:52 2022

@author: bknorris
"""

def cap_text(text):
    '''
    Input a string
    Output capitalized string
    
    NOTE: the original code used 'capitalize'
    which only capitalizes the first letter of an input string.
    'title' capitalizes all first letters after whitespace in an input string.

    '''
    #return text.capitalize()
    return text.title()
    