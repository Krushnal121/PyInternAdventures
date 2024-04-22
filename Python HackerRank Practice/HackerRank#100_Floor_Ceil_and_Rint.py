'''
Task
You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .

Note
In order to get the correct output format, add the line  below the numpy import.

Input Format

A single line of input containing the space separated elements of array .

Output Format

On the first line, print the  of A.
On the second line, print the  of A.
On the third line, print the  of A.

Problem Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
'''

import numpy
numpy.set_printoptions(sign=' ')
a = numpy.array(input().split(),float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))