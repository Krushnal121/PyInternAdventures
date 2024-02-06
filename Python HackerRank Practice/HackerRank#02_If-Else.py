'''
Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

Input Format
A single line containing a positive integer,n.
Constraints: 1<=n<=100

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

Problem Link: https://www.hackerrank.com/challenges/py-if-else
'''

n=int(input())
if n%2!=0:print("Weird")
elif n%2==0 and n in range(2,6):print("Not Weird")
elif n%2==0 and n in range(6,21):print("Weird")
elif n%2==0 and n>20:print("Not Weird")
