'''
You are given an integer,N. Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

Problem Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''

def print_rangoli(size):
    str=[chr(i) for i in range(97,97+size)]
    str.reverse()
    width=(size*2-1)*2-1
    for i in range (size):
        templst=[str[k] for k in range(i+1)]
        templst=templst+[templst[k] for k in range(len(templst)-2,-1,-1)]
        print("-".join(templst).center(width,"-"))
    for i in range (size-2,-1,-1):
        templst=[str[k] for k in range(i+1)]
        templst=templst+[templst[k] for k in range(len(templst)-2,-1,-1)]
        print("-".join(templst).center(width,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)