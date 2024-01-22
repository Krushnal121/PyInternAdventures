#find length of string in python.

#approach 1
print(f"Approach 1: The length of the string is: {len(input('Enter a string: '))}\n")

#approach 2
count=0
for i in (input('Enter a string: ')): count+=1
print(f"Approach 2: The length of the string is: {count}\n")

#approach 3
print(f"Approach 3: The length of the string is: {((input('Enter a string:')+'')).rindex('')}\n")

#approch 4
print(f"Approach 4: The length of the string is: {((input('Enter a string:')+'')).rfind('')}\n")

#approach 5
def length_recursive(str):
    if str=="":return 0
    else:return 1+length_recursive(str[1:])
print(f"Approach 4: The length of the string is:{length_recursive(input('Enter a string: '))}")