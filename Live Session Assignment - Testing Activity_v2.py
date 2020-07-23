# -*- coding: utf-8 -*-
"""
CS 5021 | Assignment - Module 5 Live Session Exercise: Testing Activity

xxxxxx | Patrick Corbett
fwb4cx | Frederick (Will) Blickle
xxxxxx | Krissy North
xxxxxxx| Rowan Rice

Due: Friday, 24 July 2020 at 1:00pm EST

Part 1
This script contains the "BookLover" class, designed to met specs outline
in the activity instructions.

Part 2
This will be tested via unit test in spearate file/s. 
    - Minimum 2x unit tests per method, using proper descriptive names
    - do //not// need to test the __str__ method
  
Part 3
This script will be copied into a new file named "BookLoverErrors".
    - This version of the code will be modified to contain several bugs
    - We will exchange this code with another group
    - We will use our test suite on their buggy code
    - We will report (in a text file):
        “Our test suite detected X/X errors.” #our test suite
        “The other group’s test suite detected X/X errors.” #their test suite

Part 4
Thinking about our semester project for CS 5010:
    - Describe some test cases that we may need to write (i.e., do some TDD)
    - No need to write code: just describe three or four tests

Due-outs:
    - 1x text file containing the answer for Parts 3 and 4. 
"""

class BookLover:
    def __init__(self, name, email, favGenre, numBooks=0, bookLst=[]):
        #This method creates the instance
        #Mandatory args: name, email, favGenre
        #Optional args: numBooks, bookLst
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        self.bookLst = bookLst
        
        #IF numBooks is //not// specified (or is 0)
        #AND a bookLst is provided that contains books
        #THEN we want to correct self.numBooks to reflect the lenght of bookLst
        if (self.numBooks != len(self.bookLst )) and (len(self.bookLst) > 0):
            self.numBooks = len(self.bookLst)
            
    
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
        i=1 
        #^tracks progress through the for loop so the elif block is
        #triggered when the loop reaches the end of the bookLst. 
        for tup in self.bookLst:
            print("for block")
            print(tup)
            if bookName in tup:
                print("if block")
                print(self.bookLst)
                return False
                
            elif i==len(self.bookLst):
                self.numBooks += 1
                self.bookLst.append(newEntry)
                print("elif block")
                print(self.bookLst)
                return True
            i+=1  
        
    def hasRead(self, bookName):
        #Takes a book name (string) and determines if person has read it
        #i.e., is bookName in bookLst list
        #returns True if they have read it / it's in bookLst
        #returns False if they have not read it / it's //not// in booklst
        for tup in self.bookLst:
            if bookName in tup:
                return True
            else:
                return False
    
    def numBooksRead(self):
        #Takes no parameters/args
        #Returns total number of books person has read
        #Uses numBooks field
        return self.numBooks
    
    def favBooks(self):
        #Takes no parameter / args
        #Returns list of titles of person's most favorite books
        #Rating must be >3 (//not// inclusive of 3)
        favBooks = []
        for tup in self.bookLst:
            name, rating = tup
            if rating>3:
                favBooks.append(name)
        return favBooks
    
'''  
#====Main Line Testing===
#Create a BookLover and test __str__
Will = BookLover("Will", "fwb4cx", "SciFi", numBooks=1, bookLst=[("Dune", 5)])
print(Will)

#Create another BookLoever and test mismatch b/t numBooks and a non-empty bklist
Pat = BookLover("Pat", "unk", "unk", numBooks=0, bookLst=[("Unk", 3)])
print(Pat)

#Add a book that isn't in the list
Will.addBook("Not Dune", 4)
print(Will)

#Krissy's error
Will.addBook("Holes", 3)
Will.addBook("Holes", 2)
print(Will)

#Add a book that is in the list
Will.addBook("Dune", 3)
print(Will)            
        
#Test hasRead method
Will.hasRead("Dune")
Will.hasRead("Unk")  

#Test numBooksRead method
Will.numBooksRead()
Pat.numBooksRead()

#Test favBooks() method
Will.favBooks()      
Will.addBook("Dune II", 1)      
print(Will)        
Will.favBooks()    
'''  
    
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

