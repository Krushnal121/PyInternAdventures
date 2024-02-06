'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format:
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints

Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

input()
List=([int(x) for x in input().split()])
List.sort()
print(list(set(List))[-2])