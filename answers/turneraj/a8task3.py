#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 8 demonstrating the use of 'for' loops with different types of iterators by creating five different functions. 

 Created by A.J. Turner on February 14, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""

def fun1(words):
	#gives word in list and its length
	print("\nThe output for function 1:")
	for w in words:
		print("The length of", w, "is", len(w))
		
		
def fun2(statement):
	#gives each letter/character in string on new line
	print("\nThe output for function 2:")
	for letter in statement:
		print(letter)
	

def fun3(tups):
	#gives each number in tuple on new line
	print("\nThe output for function 3:")
	for d in tups:
		print(d)
	

def fun4(dic):
	#gives index value for each key in dictionary
	#modified from http://stackoverflow.com/questions/17793364/python-iterate-dictionary-by-index
	print("\nThe output for function 4:")
	for index, key in enumerate(dic):
		print(index, key)
		
		
def fun5(myset):
	#gives the items in a set
	#modified from https://www.youtube.com/watch?v=2c5w6r7Ci6U
	print("\nThe output for function 5:")
	for items in myset:
		print(items)
		
		
def main():
	#first funtion called to work with list
	words = ['fish', 'tigers', 'Louisiana', 'Poeciliidae']
	fun1(words)
	
	#second function called to work with a string
	statement = "Love Purple Live Gold"
	fun2(statement)
	
	#third function to work with tuple
	tups = (1, 2, 3, 4, 5)
	fun3(tups)
	
	#fourth function to work with dictionary
	dic = {"truck":2, "car":4}
	fun4(dic)
	
	#fifth function to work with a set where a unique elements in unordered
	#collection of objs are printed
	stuff = ["tigers", "football", "tigers", "football"]
	myset = set(stuff)
	fun5(myset)
	
if __name__ == '__main__':
    main()