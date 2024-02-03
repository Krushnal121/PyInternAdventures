'''
You are given a date. Your task is to find what the day is on that date.

Problem Link: https://www.hackerrank.com/challenges/calendar-module/problem
'''

import calendar
month, day, year = list(map(int,input().split()))
print((calendar.day_name[calendar.weekday(year, month, day)]).upper())