'''
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) is equal to k.

Constraints
All coefficients of polynomial P are integers.
x and y are also integers.

Problem Statement: https://www.hackerrank.com/challenges/input/problem
'''

(x,y)= list(map(int,input().split()))
if (eval(input()) == y):print ("True")
else:print ("False")