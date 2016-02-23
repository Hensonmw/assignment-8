# !/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 12, 2016

@author: Yuankai Dong
Task 1

Previously, you wrote a program that used a recursive function to compute the
sum of the integers from 0 to 1000 (inclusive). This time, I want you to
accomplish the same thing, but using a while loop. Compute the sum of 0 to 1000
(inclusive) in a function using while. Return the sum of these numbers to the
main loop and print the result. Write the program to include a main() function
and the ifmain statement.
'''
def mySum():
    mySum = 0 
    num = 1 
    
    while num <=1000: 
        mySum += num 
        num += 1   
       
#     #print (mySum)
    return mySum


def main():
    a=mySum()
    print('a=',a)
    
    
if __name__ == '__main__':
   main()
        