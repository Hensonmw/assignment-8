# !/usr/bin/env python
# encoding: utf-8
'''
Task 2

Above, you wrote a program that used a while loop to compute the sum of the
integers from 0 to 1000 (inclusive). This time, I want you to accomplish the
same thing, but using a for loop. Compute the sum of 0 to 1000 (inclusive) in a
function using for. Return the sum of these numbers to the main loop and print
the result. Write the program to include a main() function and the ifmain
statement.
Created on Feb 12, 2016

@author: Yuankai Dong
'''
def mySum():
    mySum = 0 
    num = 1 
    
    for num in range (1,1001): 
        mySum += num 
        num += 1   
       
#     #print (mySum)
    return mySum


def main():
    a=mySum()
    print('a=',a)
    
    
if __name__ == '__main__':
   main()
        