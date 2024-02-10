'''
You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

Problem link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
'''

from collections import OrderedDict

count = int(input())
orderedDictionary = OrderedDict()
for i in range(count):
    templst = [j for j in input().split()]
    Price = int(templst[-1])
    templst.pop()
    key = " ".join(templst)
    if key not in orderedDictionary:
        orderedDictionary[key] = Price
    else:
        orderedDictionary[key] = orderedDictionary[key] + Price

for x, y in orderedDictionary.items(): print(x, y)