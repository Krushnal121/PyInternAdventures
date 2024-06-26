'''
You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Problem Link: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
'''

import numpy
inp = list(map(int, input().split()))

print(numpy.zeros((inp), int))
print(numpy.ones((inp), int))