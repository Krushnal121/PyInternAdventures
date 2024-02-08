'''
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format:
Output a single integer, your total happiness.

Problem Link: https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    elements_arr = list(map(int, input().strip().split(' ')))

    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))

    for i in elements_arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)
'''



(N,M)=map(int,input().split())
Nintegers=[int(i) for i in input().split()]
MIntegers=[[int(i) for i in input().split()],[int(i) for i in input().split()]]
print(sum([1 for i in (Nintegers) if i in(MIntegers[0])]+[-1 for i in (Nintegers) if i in(MIntegers[1])]))
