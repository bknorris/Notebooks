# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:43:15 2022

@author: bknorris
"""

import unittest
import cap_text

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap_text.cap_text(text)
        self.assertEqual(result, 'Python')
    def test_two_word(self):
        text = 'monty python'
        result = cap_text.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()
    
'''
Create class, create function "test_one"
Call functions that you want to test and make
sure the output of the test equals some value.
'''