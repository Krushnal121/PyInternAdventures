'''
You are given a complex Z. Your task is to convert it to polar coordinates.

Problem Link: https://www.hackerrank.com/challenges/polar-coordinates/problem
'''

import cmath
cmplx = complex(input())
print(abs(cmplx))
print(cmath.phase(cmplx))