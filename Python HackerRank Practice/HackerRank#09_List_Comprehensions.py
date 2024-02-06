'''
Let's learn about List comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a List of all possible coordinates given by (i'j'k) on a 3D grid where the sum of (i+j+k) is not equal to n. Here,0<=i<=x,0<=j<=y,0<=k<=z . Please use List comprehensions rather than multiple loops, as a learning exercise.

Problem Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
'''

(x,y,z,n)=(int(input()),int(input()),int(input()),int(input()))
List=[]
for i in range (0,x+1):
    for j in range (0,y+1):
        for k in range (0,z+1):
            [List.append([i,j,k]) for k in range(0,z+1) if [i,j,k] not in List and i+j+k!=n]

print(List)

