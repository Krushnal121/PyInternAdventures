'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Problem Link: https://www.hackerrank.com/challenges/incorrect-regex/problem
'''

import re
for i in range(0,int(input())):
    try:print(bool(re.compile(input())))
    except re.error:print('False')