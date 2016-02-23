#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 8

Created by Michael Henson on 15 February 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""


def addition():
    total = 0
    for x in range(0, 1001):
        total += x
    return total


def main():
    x = addition()
    print(x)


if __name__ == '__main__':
    main()
