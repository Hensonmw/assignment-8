# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:57:05 2016

@author: Glaucia
"""
"""
Above, you wrote a program that used a while loop to compute the sum of the integers 
from 0 to 1000 (inclusive). This time, I want you to accomplish the same thing, 
but using a for loop. Compute the sum of 0 to 1000 (inclusive) in a function using for. 
Return the sum of these numbers to the main loop and print the result. 
Write the program to include a main() function and the ifmain statement.
"""

def forsum():
    """sums all the values from 1 to 1000 using a for loop"""
    #starting with 0 as a first value in sum
    result=0
    #doing a for loop to iterate through all values in a range from 1 to 1001 
    for num in range(1,1001):
        #adding the result to the new number in the range
        result=result+num
    #returning the final sum
    return result
    
def main():
    final=forsum()
    print(final)

if __name__ == "__main__":
    main()
