# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:02:18 2016

@author: Glaucia
"""
"""
In Python, we tend to use for loops over different types of iterators much more 
than while loops - they're more flexible and iterators are everywhere in Python. 
Write a program that includes 5 different functions, each of which should demonstrate 
the use of for over different types of iterators. Your program should include these five 
functions, a main() function that calls all the other functions, and the ifmain statement.
"""

import numpy

def forstring():
    """prints nucleotides in a sequence that is a string"""
    #for loop to iterate thorugh the letters in the sring    
    for value in "ACTCGCCTTGGAA":
        #prints each one of the nucleotides in a different line
        print(value)
    #prints the type of the iterator
    print(type("ACTCGCCTTGGAA"))


def forlist():
    """prints nucleotides in a sequence that is a list"""
    # for loop to iterate across the values in the list
    for value in list("ACTCGCCTTGGAA"):
        #prints each one of the nucleotides in a different line
        print(value)
    #prints the type of the iterator
    print(type(list("ACTCGCCTTGGAA")))


def fortup():
    """prints nucleotides in a sequence that is a tupple"""
    #definning the tupple
    tup = ("A","C","T","C","G","C","C","T","T","G","G","A","A")
    # for loop to iterate across the values in the tupple created above
    for value in tup:
        # print the values in the tupple
        print(value)
    # prints the type of the iterator
    print(type(tup))


def fordic():
    """prints the items in a dictionary"""
    #creating the dictionary and storing it in the varable dic
    dic={"base1":"A","base2":"C","base3":"T","base4":"C","base5":"G","base6":"C"}
    # for loop to iterate across the values in the dictionary created above
    for value in dic.items():
        #prints each one of the items in the dictionary (key and value) in a different line
        print(value)
    #prints teh type of the iterator
    print(type(dic))


def fornparray():
    """prints the values in a numpy array"""
    #creating a numpy array and stroing it in a variable
    narray=numpy.array([1,2,3,4,5,6,7,8,9,10])
    #for loop to iterate across values in a numpy array
    for value in narray:
        #prints each one of the values in a different line
        print(value)
    #prints the type of the iterator
    print(type(narray))
    

def main():
    forstring()
    forlist()
    fortup()
    fordic()
    fornparray()
    
if __name__ == "__main__":
    main()

