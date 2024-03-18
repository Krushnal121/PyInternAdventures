'''
You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Problem Link: https://www.hackerrank.com/challenges/validate-a-roman-number/problem
'''

import re
digits = '(V?[I]{0,3}|I[VX])'
tens = '(L?[X]{0,3}|X[LC])'
hundreds = '(D?[C]{0,3}|C[DM])'
thousands = 'M{0,3}'
regex_pattern = thousands + hundreds + tens + digits +'$'

import re
print(str(bool(re.match(regex_pattern, input()))))