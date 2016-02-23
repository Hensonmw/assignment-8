#! /usr/bin/env python
# encoding: utf-8

'''
Five different functions demonstrating the use of "for" over
different types of iterators (ie string, list, sequence, lines,
tuple or numpy array)

Code ideas borrowed from:

http://pythonforbiologists.com/
index.php/sorting-dna-sequences-by-length-using-python/

http://biopython.org/wiki/Seq
'''

from numpy import array


def zip_iterator():
    letter = 'abc'
    number = [0, 1, 2]
    for pair in zip(letter, number):
        print("The output of zip is tuples: " + str(pair))


def list_iterator(x):
    'this program screens the length on DNA strands'
    'an example of a list iterator'
    seqs = [
    'ATAGCTGATCGTAGCTACGTACGATCG',
    'CATCGTACATGC',
    'TATGTGT',
    'GCTGATCGTGACTGTAC',
    'ACTGT',
    ]
    for seq in seqs:
        if len(seq) <= x:
            print("This sequence is too short: " + seq)
        else:
            print("This sequence is acceptable: " + seq)


def numpy_array_iterator():
    my_array = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    for element in my_array[:, 1]:
        print(element)
    print("Who do we appreciate?")


def tuple_iterator():
    letter = 'abc'
    number = [0, 1, 2]
    tuples = list(zip(letter, number))
    for letter, number in tuples:
        print(number, letter)


def set_iterator():
    'this program prints the length of unique sequences'
    'an example of a set iterator'
    seqs = {
    'ATAGCTGATCGTAGCTACGTACGATCG',
    'CATCGTACATGC',
    'TATGTGT',
    'GCTGATCGTGACTGTAC',
    'ACTGT',
    }
    for seq in seqs:
        print("The length of" + " '" + str(seq) + "\' is: " + str(len(seq)))


def main():
    list_iterator(5)
    set_iterator()
    tuple_iterator()
    numpy_array_iterator()
    zip_iterator()

if __name__ == '__main__':
    main()
