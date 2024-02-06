'''
Given an integer,n, print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description
Complete the print_formatted function in the editor below.
print_formatted has the following parameters:
int number: the maximum value to print
Prints
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Problem Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
'''

def print_formatted(number):
    lengthb = len(f"{number:b}") + 1

    for i in range(1, number + 1):
        print(f"{i:d}".rjust(lengthb - 1) + f"{i:o}".rjust(lengthb) + f"{i:X}".rjust(lengthb) + f"{i:b}".rjust(lengthb))
    # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)