#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using a for loop to sum the values from 0-1000 (inclusive).

Created by Alicia Reigel. 15 February 2016.
Copyright Alicia Reigel. Louisiana State University. 15 February 2016.

"""

def forloop_sum(arg1, arg2):
    """calculates the sum of all integers between 0 and x if x<=1000"""
    for x in range(arg1, arg2+1):
        if x<=arg2:
            the_sum=((x*(x+1))/2)
    return the_sum

def main():
    y=forloop_sum(0, 1000)
    print(y)

if __name__ == '__main__':
     main()
