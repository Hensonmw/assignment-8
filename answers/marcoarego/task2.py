#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Wed Jan 27 13:30:28 2016

@author: Marco

© 2016 MARCO A REGO ALL RIGHTS RESERVED
"""

'''
Task 2

Above, you wrote a program that used a while loop to compute the sum of the 
integers from 0 to 1000 (inclusive). This time, I want you to accomplish the 
same thing, but using a for loop. Compute the sum of 0 to 1000 (inclusive) in a
function using for. Return the sum of these numbers to the main loop and print 
the result. Write the program to include a main() function and the ifmain 
statement.
'''


def for_sum(initial_value, final_value):
    '''
    This function will calculate the sum of a range of numbers using a For Loop
    '''    
    sum_num = 0
    for num in range(initial_value, final_value+1):
        sum_num += num
    return sum_num
    

def main():
    x = for_sum(0, 1000)
    print(x)
    
    
if __name__ == '__main__':
    main()