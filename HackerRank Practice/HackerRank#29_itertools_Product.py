'''
You are given a two lists A and B. Your task is to compute their cartesian product AXB.
Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

Problem Link: https://www.hackerrank.com/challenges/itertools-product/problem
'''

(A, B) = (input().split(" "), input().split(" "))
for i in A:
    for j in B: print(f"({i}, {j})", end=" ")
