'''
The given mobile numbers may have ,  or  written before the actual  digit number. Alternatively, there may not be any prefix at all.

Input Format

The first line of input contains an integer , the number of mobile phone numbers.
 lines follow each containing a mobile number.

Output Format

Print  mobile numbers on separate lines in the required format.

Problem Link: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
'''

def wrapper(f):
    def fun(l):
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)