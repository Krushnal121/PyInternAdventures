'''
Input Format
One line of input: an integer N.
Output Format
A list on a single line containing the cubes of the first N fibonacci numbers.

Problem Link: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
'''

cube = lambda x: x**3 # complete the lambda function
def fibonacci(n):
    array=[]
    for i in range(n):
        if len(array)==0:
            array.append(0)
        elif array[-1]==0:
            array.append(1)
        else:
            array.append(array[-2]+array[-1])
    return array
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))