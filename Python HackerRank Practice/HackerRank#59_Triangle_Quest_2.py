'''
You are given a positive integer .
Your task is to print a palindromic triangle of size .

For example, a palindromic triangle of size  is:

1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Problem Link: https://www.hackerrank.com/challenges/triangle-quest-2/problem
'''

for i in range(1, int(input())+1):print(((10**i)//9)**2)