'''
Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).

Problem Link: https://www.hackerrank.com/challenges/python-tuples/problem
'''

r=int(input())
lst=input().split(" ")
for f in range(r):
    lst[f]=int(lst[f])
print(hash(tuple(lst)))