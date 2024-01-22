#Write a Python program to sum all the items in a list.

#Approach 1
#print(f"Sum of all numbers is: {sum([float(x) for x in input('Enter numbers seperated by space: ').split()])}")

#Approach 2
numlist=[]
sum=0.0
flag=True
while flag==True:
    x=input("Enter a number or type 's' to calculate sum of all numbers : ")
    if (x != 's') and (x != 'S'): numlist.append(x)
    else:
        for i in numlist:sum+=float(i)
        flag=False
print(f"The sum of all numbers is: {sum}")