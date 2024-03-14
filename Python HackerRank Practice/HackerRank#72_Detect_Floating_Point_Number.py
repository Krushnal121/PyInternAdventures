'''
You are given a string N.
Your task is to verify that N is a floating point number.

Problem Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem
'''
for i in range(int(input())):
    try:
        if float(input())!=0.0:print(True)
        else:print(False)
    except:
        print(False)
