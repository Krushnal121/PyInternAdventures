'''
You are given a positive integer . Print a numerical triangle of height  like the one below:

1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

Problem Link: https://www.hackerrank.com/challenges/python-quest-1/problem
'''

for i in range(1, int(input())):
    print((10**(i)//9)*i)