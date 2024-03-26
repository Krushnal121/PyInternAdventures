'''
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.

Problem Link: https://www.hackerrank.com/challenges/validating-uid/problem
'''

import re


def valid_uid(uid):
    if len(re.findall(r"[A-Z]", uid)) < 2 or \
            len(re.findall(r"[0-9]", uid)) < 3 or \
            not re.match(r"[A-Za-z0-9]{10}$", uid) or \
            len(set(uid)) != len(uid):
        return False

    return True


n = int(input())
for _ in range(n):
    uid = input()
    if valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")