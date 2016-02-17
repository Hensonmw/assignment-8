#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Wed Jan 27 13:30:28 2016

@author: Marco

© 2016 MARCO A REGO ALL RIGHTS RESERVED
"""

''' 
Task 3

In Python, we tend to use for loops over different types of iterators much more
than while loops - they're more flexible and iterators are everywhere in 
Python. Write a program that includes 5 different functions, each of which 
should demonstrate the use of for over different types of iterators. Your 
program should include these five functions, a main() function that calls all 
the other functions, and the ifmain statement.
'''

# Importing modules
import numpy


# Iterables functions
def list_iterator():
    list_1 = [1, 2, 3, 4]
    # I placed my iterations in my 'return' statements. In the answers each 
    # value of the iterable will be inside a list.
    return type(list_1), [x for x in list_1]


def string_iterator():
    string = 'BANANAS'
    # I placed my iterations in my 'return' statements. In the answers each 
    # value of the iterable will be inside a list.
    return type(string), [x for x in string]
    
    
def tuple_iterator():
    tuple_1 = (1, 2, 3, 4)
    # I placed my iterations in my 'return' statements. In the answers each 
    # value of the iterable will be inside a list.
    return type(tuple_1), [x for x in tuple_1]
    
    
def dictionary_iterator():
    dictionary = {'Trogon':'Trogonidae','Batara':'Thamnophilidae',
                  'Rupicola':'Cotingidae'}
    # I placed my iterations in my 'return' statements. In the answers each 
    # value of the iterable will be inside a list.
    return type(dictionary), [x for x in dictionary]


def numpy_array_iterator():
    array_numpy = numpy.array(range(10))
    # I placed my iterations in my 'return' statements. In the answers each 
    # value of the iterable will be inside a list.
    return type(array_numpy), [x for x in array_numpy]


# Main Function with print statements
def main():
    list_1 = list_iterator()
    print(list_1)
    string = string_iterator()
    print(string)
    tuple_1 = tuple_iterator()
    print(tuple_1)
    dictionary = dictionary_iterator()
    print(dictionary)
    numpy_array = numpy_array_iterator()
    print(numpy_array)
    

if __name__ == '__main__':
    main()