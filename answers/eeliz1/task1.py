#!/usr/bin/env python
# encoding: utf-8

"""
Iteration Assignment

Program to compute the sum of the integers from 0 to 1000 using a while loop.

Elisa Elizondo
"""

def sumwhile(x):
    i = 0
    while i<1000:
        i+=1
        x+=i
    return x

def main():
    x = 0
    print (sumwhile(x))

if __name__ == '__main__':
    main()
