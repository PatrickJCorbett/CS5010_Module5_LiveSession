#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS 5021 | Assignment - Module 5 Live Session Exercise: Testing Activity

pjc8cq | Patrick Corbett
fwb4cx | Frederick (Will) Blickle
kn3gs  | Krissy North
mar7dh | Rowan Rice

Due: Friday, 24 July 2020 at 1:00pm EST

Part 3
This script will be copied into a new file named "BookLoverErrors".
    - This version of the code will be modified to contain several bugs
    - We will exchange this code with another group
    - We will use our test suite on their buggy code
    - We will report (in a text file):
        “Our test suite detected X/X errors.” #our test suite
        “The other group’s test suite detected X/X errors.” #their test suite


"""

class BookLoverErrors:
    def __init__(self, name, email, favGenre, numBooks=0, bookLst= None):
        #This method creates the instance
        #Mandatory args: name, email, favGenre
        #Optional args: numBooks, bookLst
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        if bookLst is None:
            self.bookLst = []
        else:
            self.bookLst = bookLst

        #IF numBooks and the length of the bookLst do not match, correct
        #self.numBooks to reflect the length of bookLst
        if (self.numBooks != len(self.bookLst)):
           self.numBooks = len(self.bookLst)
            
        self.numBooks = numBooks + 1 ## ERROR #1
        
    
    def __str__(self):
        #This returns a string summary of the object
        #At a minimum, it must return name and bookLst
        line1 = "\nName: {}".format(self.name)
        line2 = "\nBook List: {}".format(self.bookLst)
        line3 = "\nNumber of books read: " + str(self.numBooks)
        return line1 + line2 + line3
    
    def addBook(self, bookName, rating):
        #Takes bookName and rating and tries to add to bookLst
        #! only add the book if it is not already in list
            #^only need to match on book name, not rating
        #returns True if book is added
        #returns False if book is //not// added
        newEntry = (bookName, rating)
        
        if self.hasRead(bookName):
            print("Book is already in list, cannot add again")
            return False 
        else:
            self.numBooks += 2 ## ERROR #5
            #self.bookLst.append(newEntry) ## ERROR #6
            print("Added {} to list with rating {}".format(bookName, rating))
            return True
        
    def hasRead(self, bookName):
        #Takes a book name (string) and determines if person has read it
        #i.e., is bookName in bookLst list
        #returns True if they have read it / it's in bookLst
        #returns False if they have not read it / it's //not// in booklst
        books = [x[0] for x in self.bookLst]
        
        if bookName in books:
            return False  ## ERROR #2
        else:
            return True   ## ERROR #2
        
    def numBooksRead(self):
        #Takes no parameters/args
        #Returns total number of books person has read
        #Uses numBooks field
        return (self.numBooks + 1) ## ERROR #4
    
    def favBooks(self):
        #Takes no parameter / args
        #Returns list of titles of person's most favorite books
        #Rating must be >3 (//not// inclusive of 3)
        favBooks = [x[1] for x in self.bookLst if x[1] > 3] ## ERROR #3
        return favBooks
    

       

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


