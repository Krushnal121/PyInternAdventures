'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Problem Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
'''

print(input().translate(str.maketrans(" ","-",)))