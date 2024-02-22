'''
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
Problem Link: https://www.hackerrank.com/challenges/most-commons/problem
'''

strlst=sorted([i for i in input()])
strset=set(strlst)
strdict={}
for i in strset:
    count=0
    for j in strlst:
        if i==j:
            count+=1
    strdict[i]=count
strdict=sorted(strdict.items(), key=lambda x:x[1],reverse=True)
for i in range(3):
    print(f"{strdict[i][0]} {strdict[i][1]}")