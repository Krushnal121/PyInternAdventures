'''
You are given three integers: a, b, and c. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Problem Link: https://www.hackerrank.com/challenges/python-power-mod-power/problem
'''

a,b,c=int(input()),int(input()),int(input())
print(pow(a,b))
print(pow(a,b,c))