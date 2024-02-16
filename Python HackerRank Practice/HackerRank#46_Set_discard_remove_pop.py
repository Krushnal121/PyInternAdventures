'''
You have a non-empty set s, and you have to execute N commands given in  lines.
The commands will be pop, remove and discard.

Problem Statement: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = list(map(str, input().split()))
    if command[0] == "pop":s.pop()
    elif command[0] == "remove":
        try:s.remove(int(command[1]))
        except:continue
    elif command[0] == "discard":
        try:s.discard(int(command[1]))
        except:continue
print(sum(s))