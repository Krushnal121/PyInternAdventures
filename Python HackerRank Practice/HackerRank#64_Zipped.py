'''
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5

Problem Link: https://www.hackerrank.com/challenges/zipped/problem
'''

lst1 = list(map(int, input().split()))
finlist = []
for i in range(lst1[0]):
    finlist.append(0)
for i in range(lst1[1]):
    templist = list(map(float, input().split()))
    for j in range(lst1[0]):
        finlist[j] = finlist[j] + templist[j]
for i in finlist:
    print(i / lst1[1])