'''
Task:
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format:
Read year, the year to test.

Output Format:
The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Problem Link: https://www.hackerrank.com/challenges/write-a-function
'''

def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):return True
    else: return False

year = int(input())
print(is_leap(year))