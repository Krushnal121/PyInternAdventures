'''
You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Problem Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
'''

from itertools import combinations_with_replacement
String,String_Length=input().split()
for i in combinations_with_replacement(sorted(String),int(String_Length)):
    print("".join(i))