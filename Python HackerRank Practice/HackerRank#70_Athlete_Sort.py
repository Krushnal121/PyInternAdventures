'''
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

Problem Link: https://www.hackerrank.com/challenges/python-sort-sort/problem
'''

lenbreadth=list(map(int,input().split()))
table=[]
for i in range(lenbreadth[0]):
    table.append(list(map(int,input().split())))
keys=int(input())
table.sort(key=lambda x : x[keys])

for i in range(lenbreadth[0]):
    for j in range(lenbreadth[1]):
        print(table[i][j],end=" ")
    print("\n",end="")