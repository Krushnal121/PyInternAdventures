'''
Your task is to sort the string  in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Problem Link: https://www.hackerrank.com/challenges/ginorts/problem
'''

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')