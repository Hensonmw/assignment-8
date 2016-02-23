#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 8

Created by Michael Henson on 15 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""


def addition(list):
    total = 0
    for x in list:
        total += x
    return total


def old():
    for x in range(0, 51):
        if (x % 5 == 0):
            print(x)


def silly(names):
    for x in names:
        return x


def cmore():
    for x in range(0, 24):
        if x == 8:
            return "Das Boot"


def me():
    num = 1, 2, 3
    for x in num:
        repeat = num * 10
        return repeat


def main():
    #run 1
    list = [2, 3, 5, 6]
    x = addition(list)
    print(x)
    #Run2
    old()
    #Run3
    names = ["Go State"]
    x3 = silly(names)
    print(x3)
    #Run4
    x4 = cmore()
    print(x4)
    #run5
    x = me()
    print(x)

if __name__ == '__main__':
    main()
