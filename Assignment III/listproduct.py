#Write a Python program to calculate product of all the items in a list.

#Approach 1
numlist1=[float(x) for x in input('Enter numbers seperated by space: ').split()]
product=1.0
for i in numlist1:product*=i
print(f"The product of all numbers is :{product}")

#Approach 2
numlist2=[]
product=1.0
flag=True
while flag==True:
    x=input("Enter a number or type 'p' to calculate product of all numbers : ")
    if (x != 'p') and (x != 'P'): numlist2.append(x)
    else:
        for i in numlist2:product*=float(i)
        flag=False
print(f"The product of all numbers is: {product}")