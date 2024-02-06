'''
Task:
You are given two values a and b.
Perform integer division and print .

Problem Link: https://www.hackerrank.com/challenges/exceptions/problem
'''

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)