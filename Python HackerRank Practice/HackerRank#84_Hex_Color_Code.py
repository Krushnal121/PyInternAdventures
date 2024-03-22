'''
The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

Problem Link: https://www.hackerrank.com/challenges/hex-color-code/problem
'''

import re
for _ in range(int(input())):
    result = re.findall(r"(?<=.)#[a-fA-F0-9]{3,6}", input())
    if result:
        print(*result, sep="\n")