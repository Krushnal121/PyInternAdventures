'''
Read in two integers,  and , and print three lines.
The first line is the integer division  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: .
The third line prints the divmod of  and .

Problem Link: https://www.hackerrank.com/challenges/python-mod-divmod/problem
'''

ans=divmod(int(input()),int(input()))
for i in ans: print(i)
print(ans)