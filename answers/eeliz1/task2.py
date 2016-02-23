#!/usr/bin/env python
# encoding: utf-8

"""
Iteration Assignment

Program to compute the sum of the integers from 0 to 1000 using a for loop.

Elisa Elizondo
"""

def sumfor(x):
    for i in range(0,1001):
        x+=i
    return x

def main():
    x = 0
    print(sumfor(x))

if __name__ == '__main__':
    main()
