'''
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Problem link: https://www.hackerrank.com/challenges/py-set-add/problem
'''

print(len(set([input() for i in range (int(input()))])))