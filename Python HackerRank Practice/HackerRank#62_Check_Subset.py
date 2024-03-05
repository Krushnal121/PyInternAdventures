'''
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False

Problem Link: https://www.hackerrank.com/challenges/py-check-subset/problem
'''

for i in range (int(input())):
    input()
    A=input().split()
    input()
    B=input().split()
    flag=True
    for j in A:
        if j not in B: flag=False
    print(flag)