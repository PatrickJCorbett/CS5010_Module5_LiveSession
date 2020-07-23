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
        print(Will.bookLst)
        print(Will.hasRead("Holes"))
        # Test
        self.assertEqual(Will.hasRead("Holes"), True)
 
    def test_is_hasRead_verifying_notRead_correctly(self):
        # Is hasRead() method successfully verifying non-read
        # books from the bookLst attribute of the BookLover object 

        # Set up
        WillAgain = BookLover("Will", "fwb4cx", "SciFi", numBooks=1, bookLst=[("Dune", 5)]) # create instance
        WillAgain.addBook("Not Dune", 4)
        WillAgain.addBook("Holes", 3)
        WillAgain.addBook("Dune", 2)
        print(WillAgain.bookLst)
        # Test
        self.assertEqual(WillAgain.hasRead("Not Holes"), False)

class addBookTestCase(unittest.TestCase):

    def test_addBook_is_adding_books_correctly(self):
        #Is the addBook method correctly adding books

        #Set up
        Patrick = BookLover("Patrick","pjc8cq","Fantasy")
        Patrick.addBook("Lord of the Rings", 5)
        Patrick.addBook("A Game of Thrones", 5)

        #Test
        listshouldbe = [("Lord of the Rings", 5),("A Game of Thrones", 5)]
        self.assertEqual(Patrick.bookLst, listshouldbe)
     
    def test_addBook_behaves_right_when_book_already_in_list(self):
        #Does the addBook method appropriately fail and notify
        #user when book is already in the list

        #Set up
        OtherPatrick = BookLover("Patrick","pjc8cq","Fantasy")
        OtherPatrick.addBook("The Gunslinger", 4)

        #Test
        self.assertEqual(OtherPatrick.addBook("The Gunslinger", 4), False)

class numBooksReadTestCase(unittest.TestCase):
    def test_numBooksRead_works_after_initialization(self):
        #Test that numBooksRead works correctly right after initializing
        #a BookLover
        #Set up
        Krissy = BookLover("Krissy", "kn3gs", "Nonfiction", numBooks = 2, bookLst = [("Sapiens",4),("Hamilton", 3)])
        numshouldbe = 2

        #Test
        self.assertEqual(Krissy.numBooksRead(), numshouldbe)
    
    def test_numBooksRead_works_when_initial_parameters_disagree(self):
        #Test that numBooksRead is still correct if the initial
        #numBooks is not the length of bookLst.
        AlsoKrissy = BookLover("Krissy","kn3gs","Nonfiction",numBooks = 10, bookLst = [("Sapiens", 4)])
        numshouldbe = 1

        #Test
        self.assertEqual(AlsoKrissy.numBooksRead(), numshouldbe)

    def test_numBooksRead_works_after_adding_book(self):
        #Test that after adding a book, the numBooksRead method
        #still functions correctly

        #Set up
        KrissyAgain = BookLover("Krissy", "kn3gs","Nonfiction")
        KrissyAgain.addBook("Sapiens", 4)
        numshouldbe = 1

        #Test
        self.assertEqual(KrissyAgain.numBooksRead(), numshouldbe)

class favBooksTestCase(unittest.TestCase):
    def test_favBooks_works_when_there_are_favorites(self):
        #Test whether the favBooks method works when there are
        #entries with a rating of 4 or higher
    
        Rowan = BookLover("Rowan","mar7dh","violent historical dramas")
        Rowan.addBook("Peaky Blinders", 5)
        Rowan.addBook("Peaky Blinders without subtitles", 3)

        fav_list_should_be = ["Peaky Blinders"]
        
        #Test
        self.assertEqual(Rowan.favBooks(), fav_list_should_be)

    def test_favBooks_works_when_there_are_no_favorites(self):
        #Test whether the favBooks method correctly returns
        #a blank list when there are no entries with a rating 
        #higher than 3

        #Set up
        RowanAgain = BookLover("Rowan","mar7dh","violent historical dramas")
        RowanAgain.addBook("Peaky Blinders without subtitles", 3)
        RowanAgain.addBook("insert random title here", 2)

        fav_list_should_be = []

        #Test
        self.assertEqual(RowanAgain.favBooks(), fav_list_should_be)    
    

if __name__ == '__main__':
    unittest.main()   