# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:20:23 2016

@author: Glaucia
"""
"""
Previously, you wrote a program that used a recursive function to compute the 
sum of the integers from 0 to 1000 (inclusive). This time, I want you to accomplish 
the same thing, but using a while loop. Compute the sum of 0 to 1000 (inclusive) 
in a function using while. Return the sum of these numbers to the main loop and print
 the result. Write the program to include a main() function and the ifmain statement.
 
"""
def whilesum():
    """sums all the numbers in a range from 0 to 1000 """
    #setting an initial value for the variable result
    result=0
    #setting an initial value for the counter
    num=0
    #defining a while loop to keep adding the values while the counter is still less than 1001
    while num < 1001:
        #adding the values from 1 to 1001 to the variable result
        result=result+num
        #adding 1 to the counter
        num=num+1
    #returning the final result
    return result
    
def main():
    final=whilesum()
    print(final)

if __name__ == "__main__":
    main()

