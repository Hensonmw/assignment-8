#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 8

Created by Michael Henson on 15 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""


def addition():
    x = 0
    total = 0
    while x < 1000:
        x += 1
        total += x
    return total


def main():
    x = addition()
    print(x)


if __name__ == '__main__':
    main()
