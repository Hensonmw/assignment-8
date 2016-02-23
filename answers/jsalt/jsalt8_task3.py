#!/usr/bin/env python
# utf-8

"""
Assignment 8
Task 3 Program: Different Types of Iterators
Jessie Salter
12 February 2016
"""

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


def for_str(word, count, character):
    '''Counts and prints the number of times a character appears in a word'''
    for letter in word:
        if letter == character:
            count += 1
    print(count)


def for_dct(word):
    '''Counts and prints the number of times each letter appears in a word \
    based on Think Python chapter 11.2 \
    (http://www.greenteapress.com/thinkpython/)'''
    d = dict()
    for letter in word:
        count = d.get(letter, 0)
        d[letter] = 1 + count
    print(d)


def for_seq(seq_list):
    '''Concatenates multiple sequences. Adapted from BioPython documentation \
    section 3.5 \
    (http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc28)'''
    concatenated = Seq("", generic_dna)
    for s in seq_list:
        concatenated += s
    print(concatenated)


def for_file(my_file):
    with open(my_file) as poem:
        for line in poem:
            print(line)


def for_list(forecast):
    '''Converts temperatures from farenheit to celsius'''
    for temp in forecast:
        celsius = (temp - 32) * (5/9)
        print(int(celsius))


def main():
    for_str("mississippi", 0, "s")
    for_dct("mississippi")
    for_seq([Seq("ACGT", generic_dna), Seq("ATATAT", generic_dna)])
    for_file('poem.txt')
    for_list(list([32, 45, 60, 75]))

if __name__ == '__main__':
    main()
