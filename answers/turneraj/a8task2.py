#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 8 demonstrating the use of 'for' in a function to compute the sum of 0 to 1000. Modified from Brant Faircloth's lecuture.

 Created by A.J. Turner on February 14, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""

def forsum(x):
	for i in range(0,1001): #for loop to compute sum over a range
		x += i
	return x 

	
def main():
	x = 0
	print("The sum of integers from 0 to 1000 is:", forsum(x))

if __name__ == '__main__':
    main()