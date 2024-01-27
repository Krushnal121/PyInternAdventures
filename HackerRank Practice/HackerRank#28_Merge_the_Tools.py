'''
Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

def merge_the_tools(string, k):
    lst=[string[i-k:i] for i in range(k,len(string)+1,k)]
    for i in lst:
        tmplst=[]
        for j in i:
            if j not in tmplst:
                tmplst.append(j)
        print("".join(tmplst))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)