'''
Perform append, pop, popleft and appendleft methods on an empty deque d.

Problem Link: https://www.hackerrank.com/challenges/py-collections-deque/problem
'''

from collections import deque
DQ=deque()
for i in range(int(input())):
    command=input().split()
    if command[0]=="append":DQ.append(int(command[1]))
    elif command[0]=="appendleft":DQ.appendleft(command[1])
    elif command[0]=="pop":DQ.pop()
    elif command[0]=="popleft":DQ.popleft()
for i in DQ:print(i,end=" ")