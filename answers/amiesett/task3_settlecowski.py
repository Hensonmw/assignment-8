#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 8 Task 3

Amie Settlecowski
16 Feb. 2016

This program demonstrates the use of for loops over 5 types of iterables
"""


import task1_assign6
import numpy as np


def loop1(ls):
    # for loop over list
    # defines corresponding list of oddness/evenness for every item in ls
    ls_odd_even = []
    for item in ls:
        num_type = task1_assign6.odd_even(item)
        ls_odd_even.append(num_type)
    return ls_odd_even


def loop2(dct):
    # for loop over dictonary keys
    # enters odd, even, or 0 values corresponding to keys in dictionary
    for num in dct:
        num_type = task1_assign6.odd_even(num)
        dct[num] = num_type
    return dct


def loop3(string):
    # for loop over characters in string
    # writes and returns string w/out vowels
    strng = ''
    for char in string:
        if char not in ['a', 'e', 'i', 'o', 'u']:
            strng += char
        else:
            pass
    return strng


def loop4(ifile):
    # demonstrates for loop over lines in a file
    # prints every line in a file
    for line in ifile:
        print(line)


def loop5(matrix):
    # demonstrates for loop over rows of numpy array
    # adds row number to the entry where row # == column #
    count = 0
    for row in matrix:
        row[count] += (count + 1)
        count += 1
    return matrix


def main():
    # 1 for loop over list of integers
    ls = list(range(1, 5))
    print("list BEFORE iteration through for loop\n", ls)
    ls_odd_even = loop1(ls)
    print("list AFTER iteration through for loop\n", ls_odd_even, '\n')

    # 2. for loop over dictionary of integers
    dct = dict.fromkeys(ls, None)
    print("dictionary BEFORE iteration through for loop\n", dct)
    dct = loop2(dct)
    print("dictionary AFTER iteration through for loop\n", dct, '\n')

    # 3. for loop over characters in a string
    string = 'alphabet'
    print("string BEFORE iteration through for loop\n", string)
    string = loop3(string)
    print("string AFTER iteration through for loop\n", string, '\n')

    # 4. for loop over lines in a file
    # opening file, python_poem.txt, in read mode
    with open('python_poem.txt', 'r') as ifile:
        # check that ifile opens in read mode w/out error
        if ifile.readable() == 'False':
            ifile.close()
        else:
            pass
        loop4(ifile)
        ifile.close()

        # 5. for loop over rows of numpy array
        matrix = np.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])
        print("numpy array BEFORE iteration through for loop\n", matrix)
        matrix = loop5(matrix)
        print("numpy array AFTER iteration through for loop\n", matrix)

if __name__ == '__main__':
    main()
