'''
You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

Input Format
The first line contains the space separated values of  and .
The next  lines contains the space separated elements of  columns.

Output Format
First, print the transpose array and then print the flatten.

Problem Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
'''

import numpy
narr = numpy.array([input().split() for _ in range(int(input().split()[0]))],int)
print (narr.transpose())
print (narr.flatten())