#!/usr/bin/env python
# #encoding: utf-8

"""
Program made that includes 5 different functions, each of which
demonstrates the use of for loops to iterate over different types of iterators.
Thats a mouthful....

Created by Alicia Reigel. 15 February 2016.
Copyright Alicia Reigel. Louisiana State University. 15 February 2016.

"""
import numpy as np

def for1():
    """this function iterates over the numpy array for 456 to 571 by 10s and prints each number"""
    print("This is a for loop output for a numpy array:")
    for x in np.arange(456, 571, 10):
        print(x, end=",")
    print('\n')

def for2():
    """this function iterates over a list of letters and prints each followed by a space"""
    print("This is a for loop output for a list:")
    for x in list('pythonproblems'):
        print(x, end=" ")
    print('\n')

def for3():
    """this function iterates over a string and prints each letter"""
    print("This is a for loop output for a string:")
    for x in ("ACCTTGGCTAG"):
        print(x)


def for4():
    """this function iterates over a range and prints each value"""
    print("This is a for loop output for a range:")
    for x in range(0,10):
        print(x)


def for5():
    """this function iterates over a tuple and prints the values"""
    #Some help was obtained from http://www.tutorialspoint.com/python/python_tuples.htm
    print("This is a for loop output for a tuple:")
    ar_tuple1=('python', 'hard', 'R', 'harder', 'c++', 'hardest')
    for x in ar_tuple1:
        print(x[0::], end=" ")


def main():
    for1()
    for2()
    for3()
    for4()
    for5()

if __name__ == '__main__':
    main()
