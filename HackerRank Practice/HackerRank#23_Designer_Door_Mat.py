'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

Input Format:
A single line containing the space separated values of  and .

Output Format:
Output the design pattern.

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
'''

height=int((input().split(" "))[0])
width=height*3
fraction_width=(width//2)-1
ranged=height//2
str=".|."
for i in range(ranged):print((i*str).rjust(fraction_width,"-")+str+(i*str).ljust(fraction_width,"-"))
print("WELCOME".center(width,"-"))
for i in range(ranged-1,-1,-1):print((i*str).rjust(fraction_width,"-")+str+(i*str).ljust(fraction_width,"-"))