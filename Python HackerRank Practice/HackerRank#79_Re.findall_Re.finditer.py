'''
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of  that contains  or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only.

Problem Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
'''

import re
m = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", input(), re.IGNORECASE)
if m:print(*m, sep="\n")
else:print(-1)