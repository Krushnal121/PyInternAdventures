'''
The first line contains a single integer,n, denoting the number of email address.
Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this format:

Problem Link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
'''

import re
import email.utils
n = int(input().strip())
temp =[]
a = re.compile(r'<[a-z0-9][\w._-]+@[a-z]+\.[a-z]{1,3}>', re.I)
for _ in range(n):
    temp.append(input().strip())
for i, x in enumerate(temp):
    v =  a.search(x)
    if v:
        print(temp[i])