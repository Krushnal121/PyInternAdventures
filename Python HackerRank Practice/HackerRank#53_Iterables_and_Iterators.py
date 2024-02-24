'''
You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.
Find the probability that at least one of the  indices selected will contain the letter: ''.

Problem Link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
'''

from itertools import combinations, groupby
count, letters, to_select = int(input()), input().split(), int(input())
letters.sort()
combinations_of_letters = list(combinations(letters, to_select))
contain = len([c for c in combinations_of_letters if 'a' in c])
print(contain / len(combinations_of_letters))