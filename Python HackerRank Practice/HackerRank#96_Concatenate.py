'''
You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns.

Output Format

Print the concatenated array of size X.

Problem Link: https://www.hackerrank.com/challenges/np-concatenate/problem
'''

import numpy as np

n, m, p = map(int, input().split())

arr_nxp = []
arr_mxp = []
for i in range(n):
    arr_nxp.append(input().split())
for j in range(m):
    arr_mxp.append(input().split())

arr3 = np.concatenate((arr_nxp, arr_mxp), axis=0)
arr3 = np.array(arr3, int)
print(arr3)
