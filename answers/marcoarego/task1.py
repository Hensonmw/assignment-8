#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Wed Jan 27 13:30:28 2016

@author: Marco

© 2016 MARCO A REGO ALL RIGHTS RESERVED
"""

'''
Task 1

Previously, you wrote a program that used a recursive function to compute the 
sum of the integers from 0 to 1000 (inclusive). This time, I want you to 
accomplish the same thing, but using a while loop. Compute the sum of 0 to 1000
(inclusive) in a function using while. Return the sum of these numbers to the
main loop and print the result. Write the program to include a main() function 
and the ifmain statement.
'''



def while_sum(initial_num, final_num):
    '''
    Function that calculates the sum of any range of numbers you want using a
    while loop
    '''    
    initial_num = 0
    num_sum = 0
    while initial_num <= final_num:
        num_sum += initial_num
        initial_num += 1
    return num_sum


def main():
    x = while_sum(0, 1000)
    print(x)


if __name__ == '__main__':
    main()

