'''
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Problem Link: https://www.hackerrank.com/challenges/piling-up/problem
'''

for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")