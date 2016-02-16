# !/usr/bin/env python
# encoding: utf-8
""" 
Write a program that includes 5 different functions, each of which should
demonstrate the use of for over different types of iterators. Your program
should include these five functions, a main() function that calls all the other
functions, and the ifmain statement.
Created on Feb 12, 2016

@author: Yuankai Dong

"""
from Bio.Seq import Seq
import numpy

def function1():#file
    count=0
    f=open('test.txt')
    for line in f.readlines():
        count += 1
           
    #count how many lines in there.
    return count
        

def function2():#list
    for list in [1,2,3,4,5,6]:
        list+=1
    return list
    
    
def function3():#string
    for string in 'A':
        string+=' is what I want'
    return string
        
        
def function4():#biopython
    my_seq = Seq('CATATAGCCATTCG')
    for seq in my_seq:
        my_seq=my_seq+my_seq    
        return my_seq
       
        
def function5():#nympy array
    a=(numpy.array([0,5,10,15,20]))
    for col in a:
        a+=1
        return a
       

def main():
    function1()
    print("\nfunction1=",function1())
    function2()
    print("\nfunction2=",function2())
    function3()
    print("\nfunction3=",function3())
    function4()
    print("\nfunction4=",function4())
    function5()
    print("\nfunction5=", function5())
    
    
if __name__ == "__main__":
    main()