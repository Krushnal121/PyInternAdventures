'''
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

For a better understanding of the problem, check the explanation.

Problem Link: https://www.hackerrank.com/challenges/compress-the-string/problem
'''

from itertools import groupby
for k, c in groupby(input()):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')