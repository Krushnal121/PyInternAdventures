'''
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.

Problem Link: https://www.hackerrank.com/challenges/py-set-mutations/problem
'''

input()
mainlst=set(list(map(int,input().split())))
for i in range (int(input())):
    lst1=input().split()
    lst2=set(list(map(int,input().split())))
    if(lst1[0]=="intersection_update"):
        mainlst.intersection_update(lst2)
    elif(lst1[0]=="symmetric_difference_update"):
        mainlst.symmetric_difference_update(lst2)
    elif(lst1[0]=="difference_update"):
        mainlst.difference_update(lst2)
    elif(lst1[0]=="update"):
        mainlst.update(lst2)

sum=0
for i in mainlst: sum+=i
print(sum)