#!/usr/bin/env python
# #encoding: utf-8

"""
Program made using a while loop to sum the values from 0-1000 (inclusive).

Created by Alicia Reigel. 14 February 2016.
Copyright Alicia Reigel. Louisiana State University. 14 February 2016.

"""

def while_sum(x):
    """calculates the sum of all integers between 0 and x if x<=1000"""
    while x>=0 and x<1001:
        y=((x*(x+1))/2)
        x=x+1
        while_sum(x)
        return y

def main():
    y=while_sum(1000)
    print(y)

if __name__ == '__main__':
     main()
