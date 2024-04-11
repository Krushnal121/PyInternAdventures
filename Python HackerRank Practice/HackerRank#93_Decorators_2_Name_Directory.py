'''
Input Format

The first line contains the integer , the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.
Output Format

Output  names on separate lines in the format described above in ascending order of age.

Problem Link: https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
'''

import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

