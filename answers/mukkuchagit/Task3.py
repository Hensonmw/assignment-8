#!/usr/bin/env python
# encoding: utf-8
"""
Iteration assignment.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import numpy as np


def list():
    emptylist = []
    for i in [1, 2, 3]:
        i += 1
        emptylist.append(i)
    return emptylist


def tuple():
    tum = ([1234], [9876], ['Hi'])
    for i in tum:
        i.append(5)
    return tum


def string():
    emptylist = []
    for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
        invitation = "Hi " + f + "! Please, come to my party on Saturday!"
        emptylist.append(invitation)
    return emptylist


def dictionary():
    basket = {'apple': 10, 'mango': 30, 'orange': 5}
    cart = 0
    buy_fruits = basket.items()
    for k, v in buy_fruits:    # k=key,v=value
        cart += v
    return cart


def numpy_array():
    emptylist = []
    for x in np.arange(6):
        x += 100
        emptylist.append(x)
    return emptylist


def main():
    v = list()
    print("Using list: ",v)
    x = tuple()
    print("Using Tuple: ",x, end='\n')
    z = string()
    print("Using String; ",z)
    y = dictionary()
    print("Using Dictionary: ",y)
    Num = numpy_array()
    print("Using Arrray: ",Num)


if __name__ == '__main__':
    main()
