# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 8
Oscar Johnson 11 February 2016
"""

import numpy as np


def sum_list(list):
    """
    sum values in a list
    """
    x = 0
    for num in list:
        x += num
    return x


def sum_string(string):
    """
    sum values in a string
    """
    x = 0
    for num in string:
        x += num
    return x


def tuple_to_list(tup):
    """
    returns the items in a tuple as a list
    """
    list = [] # list to hold our items
    for item in tup:
        list.append(item)
    return list        


def dict_to_string(dict):
    """
    takes values from a dictionary, based on the key
    and returns as a string
    """
    string = ""
    for key in dict:
        x = dict[key]
        string += str(x)
        string += ", "
    return string


def array_add(arr):
    """
    adds 2 to all values in a numpy array
    """
    for val in np.nditer(arr, op_flags=['readwrite']):
        #numpy arrays are read-only, so we need to specify readwrite
        val[...] = val + 2
    return arr


def main():
    #calls the function to sum a list
    list = [1, 2, 3, 4, 5]
    call_list = sum_list(list)
    #calls the function to sum a string
    string = (1, 2, 3, 4, 5)
    call_string = sum_string(string)
    #calls function to covert tuple to list
    tup = (2, 4, 6, 8, ": who do we appreciate?")
    list_tuple = tuple_to_list(tup)
    #calls function to extract values from dictionary and convert to string
    d = {"taxon": "Stigmatura", "habitat": "river island scrub", "num_samples": 3}
    dict_str = dict_to_string(d)
    #calls function to add 2 to all values of numpy array
    array = np.array([[1, 2], [3, 4]])
    added_array = array_add(array)
    print(" sum of list = ", call_list, "\n", 
          "sum of string = ", call_string, "\n",
          "was a tuple, now a list! ", list_tuple, "\n",
          "was a dictionary, now a string! ", dict_str, "\n",
          "array with added values: ", added_array
          )


if __name__ == '__main__':
    main()