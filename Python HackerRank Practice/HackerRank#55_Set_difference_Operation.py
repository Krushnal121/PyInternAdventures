'''
Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

Problem Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
'''

input()
set1=set(map(int,input().split()))
input()
print(len(set1.difference(set(map(int,input().split())))))