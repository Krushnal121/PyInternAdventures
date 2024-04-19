'''
Your task is to print an array of size NXM with its main diagonal elements as 's and 's everywhere else.

Problem Link: https://www.hackerrank.com/challenges/np-eye-and-identity/problem
'''

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))