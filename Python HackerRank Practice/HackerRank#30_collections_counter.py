'''
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Problem link: https://www.hackerrank.com/challenges/collections-counter/problem
'''

from collections import Counter
(count,sizedict,sumamt)=(int(input()),Counter(map(int, input().split())),0)
for i in range(int(input())):
    size, rate = map(int, input().split())
    if sizedict[size]:
        sizedict[size] -= 1
        sumamt += rate
print(sumamt)