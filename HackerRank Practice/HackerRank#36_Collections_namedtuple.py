'''
calculate the average marks of the students.
sample data:

ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Problem link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
'''

from collections import namedtuple
count = int(input())
columns = input().split()
marks_sum = 0
for _ in range(count):
    students = namedtuple('student', columns)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    marks_sum += int(student.MARKS)
print((marks_sum / count))

#This is a new linne