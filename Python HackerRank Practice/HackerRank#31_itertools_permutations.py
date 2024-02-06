'''
You are given a string s.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

Problem Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
'''

from itertools import permutations
inputval=[i for i in input().split()]
lst=[]
[lst.append("".join(i)) for i in list(permutations([i for i in inputval[0] if i.isalpha()==True],int(inputval[-1])))]
[print(i) for i in (sorted(lst))]
