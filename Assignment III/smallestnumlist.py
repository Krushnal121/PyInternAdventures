#Write a Python program to get the Smallest number from a List.

#Approach 1
numlist=([x for x in input("Approach 01: Enter the numbers seperated by a space: ").split()])
numlist.sort()
print(f"The smallest number is {numlist[0]}\n")

#Approach 2
numlist2=((input("Approach 02: Enter the numbers seperated by a space: ")).split())
currestsmallest=numlist2[0]
for i in numlist2:
    if i<currestsmallest:currestsmallest=i
print(f"The smallest number is: {currestsmallest}")
