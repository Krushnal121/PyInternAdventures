'''
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print .

Problem Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
'''

lsttarlength=[i for i in map(int, input().split())]
(lst,tar,idxlst)=([input() for i in range (lsttarlength[0])],[input() for i in range (lsttarlength[1])],[])
for i in range(len(tar)):
    idxlst.clear()
    for j in range (len(lst)):
        if tar[i] not in lst:
            idxlst.append(-1)
            break
        elif tar[i]==lst[j]:idxlst.append(j+1)
    for k in idxlst:
        if k!=idxlst[-1]:print(k,end=" ")
        else:print(k,end="\n")