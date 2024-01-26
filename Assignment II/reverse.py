#Approach 1
print(f"The reversed string is: {input('Enter a string: ')[::-1]}")

#Approach 2
str=input("Enter a string: ")
for i in range ((len(str)-1),-1,-1):print(str[i],end="")