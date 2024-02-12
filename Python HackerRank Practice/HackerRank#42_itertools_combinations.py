'''
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Problem Link: https://www.hackerrank.com/challenges/itertools-combinations/problem
'''

from itertools import combinations
string , size  = input().split()
for i in range(1, int(size)+1):
    for j in combinations(sorted(string), i):
        print (''.join(j))