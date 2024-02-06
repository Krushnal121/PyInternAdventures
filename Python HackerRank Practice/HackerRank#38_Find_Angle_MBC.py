'''
Triangle ABC is a right triangle, 90 at B.
Therefore, ABC=90.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and AC.
Your task is to find MBC (angle Theta, as shown in the figure) in degrees.

Problem Link: https://www.hackerrank.com/challenges/find-angle/problem
'''

from math import degrees, atan2
print((str(round(degrees(atan2(float(input()),float(input())))))), chr(176), sep='')