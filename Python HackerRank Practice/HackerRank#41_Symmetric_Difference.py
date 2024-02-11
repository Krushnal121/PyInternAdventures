'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Problem Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
'''

input()
list1=[i for i in map(int,input().split())]
input()
list2=[i for i in map(int,input().split())]
for i in sorted(set([i for i in list1 if i not in list2]+[i for i in list2 if i not in list1])):print(i)