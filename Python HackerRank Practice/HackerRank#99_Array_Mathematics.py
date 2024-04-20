'''
You are given two integer arrays,  and  of dimensions X.
Your task is to perform the following operations:

Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)

Problem link: https://www.hackerrank.com/challenges/np-array-mathematics/problem
'''

import numpy

N, M = map(int, input().split(' '))

a = [numpy.array((input().split(' ')), dtype='int') for i in range(N)]
b = [numpy.array((input().split(' ')), dtype='int') for j in range(N)]

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
