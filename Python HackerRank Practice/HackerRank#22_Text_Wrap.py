'''
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width .
Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to
Returns
string: a single string with newline characters ('\n') where the breaks should be

Problem Link: https://hackerrank.com/challenges/text-wrap/problem
'''

import textwrap

def wrap(string, max_width):
    outstr="\n".join(textwrap.TextWrapper(width=max_width).wrap(text=string))
    return outstr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)