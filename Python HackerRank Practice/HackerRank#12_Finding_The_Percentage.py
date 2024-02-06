'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Problem Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
'''

scoredict={}
for i in range (int(input())):
    Lst=input().split(" ")
    scoredict[Lst[0]]=[float(Lst[1]),float(Lst[2]),float(Lst[3])]
Lst=scoredict[input()]
print(format(sum(Lst)/len(Lst),'.2f'))