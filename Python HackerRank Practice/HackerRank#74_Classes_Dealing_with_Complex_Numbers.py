'''
For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.
The real and imaginary precision part should be correct up to two decimal places.

Problem Link: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
'''

import math
from math import hypot


class Complex(object):
    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary

    def __add__(self, no):
        return Complex(self.re + no.re, self.im + no.im)

    def __sub__(self, no):
        return Complex(self.re - no.re, self.im - no.im)

    def __mul__(self, no):
        return Complex(
            self.re * no.re - self.im * no.im,
            self.im * no.re + self.re * no.im)

    def __truediv__(self, no):
        return Complex(
            (self.re * no.re + self.im * no.im) / (no.re ** 2 + no.im ** 2),
            (self.im * no.re - self.re * no.im) / (no.re ** 2 + no.im ** 2))

    def mod(self):
        return Complex(hypot(self.re, self.im), 0.0)

    def __str__(self):
        return "{:.2f}{:+.2f}i".format(self.re, self.im)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')