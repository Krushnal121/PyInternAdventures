'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

Problem Link: https://www.hackerrank.com/challenges/capitalize/problem
'''

import os
def solve(s):
    output=" ".join([i.capitalize() for i in s.split(" ")])
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
