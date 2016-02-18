#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 8 demonstrating the use of 'while' in a function to compute the sum of 0 to 1000. Modified from Brant Faircloth's lecture.

 Created by A.J. Turner on February 14, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""

def whilesum(x):
	i = 0
	while i < 1000: #loop from 0 to 1000 and adding each number
		i += 1
		x += i
	return x

	
def main():
	x = 0
	print("The sum of integers from 0 to 1000 is:", whilesum(x))
	
if __name__ == '__main__':
    main()