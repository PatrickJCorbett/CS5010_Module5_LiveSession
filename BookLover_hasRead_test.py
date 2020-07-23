# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:54:02 2020

@author: kriss
"""


"""

CS 5021 | Assignment - Module 5 Live Session Exercise: Testing Activity
File: BookLover_hasRead_Test.py
    Need File: BookLover.py
​

xxxxxx | Patrick Corbett

fwb4cx | Frederick (Will) Blickle

kn3gs | Krissy North

xxxxxxx| Rowan Rice

​

Due: Friday, 24 July 2020 at 1:00pm EST

​


Part 2

This will be tested via unit test in spearate file/s. 

    - Minimum 2x unit tests per method, using proper descriptive names

    - do //not// need to test the __str__ method



"""

import unittest
from BookLover import *

class hasReadTestCase(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing hasRead() method in BookLover.py
    
    def test_is_hasRead_verifying_read_correctly(self):
        # Is hasRead() method successfully verifying read
        # books from the bookLst attribute of the BookLover object 

        # Set up
        Will = BookLover("Will", "fwb4cx", "SciFi", numBooks=1, bookLst=[("Dune", 5)]) # create instance
        Will.addBook("Not Dune", 4)
        Will.addBook("Holes", 3)
        Will.addBook("Dune", 2)
        
        # Test
        self.assertEqual(Will.hasRead("Holes"), True)
 
    def test_is_hasRead_verifying_notRead_correctly(self):
        # Is hasRead() method successfully verifying non-read
        # books from the bookLst attribute of the BookLover object 

        # Set up
        Will = BookLover("Will", "fwb4cx", "SciFi", numBooks=1, bookLst=[("Dune", 5)]) # create instance
        Will.addBook("Not Dune", 4)
        Will.addBook("Holes", 3)
        Will.addBook("Dune", 2)
        
        # Test
        self.assertEqual(Will.hasRead("Not Holes"), False)


     
if __name__ == '__main__':
    unittest.main()   