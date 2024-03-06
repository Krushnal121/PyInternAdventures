'''
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
'''

superset=input().split()
flag=True
for i in range (int(input())):
    A=input().split()
    if(len(superset)>len(A)):
        for j in A:
            if(flag==False):break
            if j in superset:flag=True
            else:flag=False
    else:flag=False
print(flag)