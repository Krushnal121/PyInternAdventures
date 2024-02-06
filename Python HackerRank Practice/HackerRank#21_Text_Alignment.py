'''
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

Problem Link: https://www.hackerrank.com/challenges/text-alignment/problem
'''

count=int(input())
str="H"
for i in range(count):print((i*str).rjust(count-1)+str+(i*str).ljust(count-1))
for i in range(count+1):print((str*count).center(count*2)+(str*count).center(count*6))
for i in range((count+1)//2):print((str*count*5).center(count*6))
for i in range(count+1):print((str*count).center(count*2)+(str*count).center(count*6))
for i in range(count):print(((str*(count-i-1)).rjust(count)+str+(str*(count-i-1)).ljust(count)).rjust(count*6))