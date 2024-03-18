'''
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Problem Link: https://www.hackerrank.com/challenges/re-start-re-end/problem
'''

import re
s, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')