'''
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Problem Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''

def average(array):
    lstset=set(array)
    avg=sum(lstset)/len(lstset)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)