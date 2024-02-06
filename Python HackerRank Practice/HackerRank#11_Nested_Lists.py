'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Problem Link: https://www.hackerrank.com/challenges/nested-list/problem
'''

List=[[input(),float(input())] for i in range (int(input()))]
namelist=[]
List.sort(key=lambda x: x[1])
def printnames(i):
    if List[0][1]==List[i][1]:
        printnames(i+1)
    else:
        if i+1!=len(List):
            if List[i][1] != List[i + 1][1]:
                namelist.append(List[i][0])
            else:
                namelist.append(List[i][0])
                printnames(i + 1)
        else:
            namelist.append(List[i][0])

printnames(1)
namelist.sort()
for i in namelist:print(i)