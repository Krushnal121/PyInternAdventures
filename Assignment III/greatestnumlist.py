#Write a Python program to get the largest number from a list.

#Approach 1
numlist=([x for x in input("Approach 01: Enter the numbers seperated by a space: ").split()])
numlist.sort(reverse=True)
print(f"The greatest number is {numlist[0]}\n")

#Approach 2
numlist2=((input("Approach 02: Enter the numbers seperated by a space: ")).split())
currentgreatest=numlist2[0]
for i in numlist2:
    if i>currentgreatest:currentgreatest=i
print(f"The Greatest number is: {currentgreatest}")
