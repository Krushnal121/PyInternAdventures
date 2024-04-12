'''
You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.
Input Format
A single line of input containing  space separated integers.
Output Format
Print the X NumPy array.

Problem Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem
'''

import numpy
array = numpy.array(list(map(int, input().strip().split())))
print(numpy.reshape(array, (3,3)))
