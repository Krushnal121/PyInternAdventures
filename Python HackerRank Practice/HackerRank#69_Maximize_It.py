'''
The first line contains  space separated integers  and .
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

Problem Link: https://www.hackerrank.com/challenges/maximize-it/problem
'''

from itertools import product
K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(sorted(list(results)))