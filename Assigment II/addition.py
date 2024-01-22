#python program to add two numbers.
print(f"The addition of the numbers you have provided is: {float(input('Enter the first number: '))+float(input('Enter the second number: '))}")

#Python program to add indefinite numbers
print(f"The sum of numbers you have provided is: {sum([float(i) for i in [x for x in input('Enter the numbers separated by spaces: ').split()]])}")