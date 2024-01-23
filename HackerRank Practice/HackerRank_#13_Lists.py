'''
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Problem Link: https://www.hackerrank.com/challenges/python-lists/problem
'''

lst=[]
for i in range (int(input())):
    lst2=input().split(" ")
    if lst2[0]=="insert":lst.insert(int(lst2[1]),int(lst2[2]))
    elif lst2[0]=="print":print(lst)
    elif lst2[0]=="remove":lst.remove(int(lst2[1]))
    elif lst2[0]=="append":lst.append(int(lst2[1]))
    elif lst2[0]=="sort":lst.sort()
    elif lst2[0]=="pop":lst.pop()
    elif lst2[0]=="reverse":lst.reverse()