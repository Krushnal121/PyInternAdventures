'''
You are given a stringS.Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Problem Link : https://www.hackerrank.com/challenges/string-validators/problem
'''

s = input()
l = len(s)
lst = [s[i:] for i in range(l)]
for i in range(l):
    if s[i] not in lst:
        lst.append(s[i])
(isalnum,isalpha,isdigit,islower,isupper) = (False,False,False,False,False)
for i in lst:
    if isalnum!=True:
        isalnum=i.isalnum()
    if isalpha!=True:
        isalpha=i.isalpha()
    if isdigit!=True:
        isdigit=i.isdigit()
    if islower!=True:
        islower=i.islower()
    if isupper!=True:
        isupper=i.isupper()
print(isalnum)
print(isalpha)
print(isdigit)
print(islower)
print(isupper)
