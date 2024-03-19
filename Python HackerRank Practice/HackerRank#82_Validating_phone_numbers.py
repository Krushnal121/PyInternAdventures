'''
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7,8 or 9.

Problrm link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
'''

for i in range(int(input())):
    no=input()
    if no[0]in("9","7","8") and len(no)==10 and no.isnumeric():print("YES")
    else:print("NO")