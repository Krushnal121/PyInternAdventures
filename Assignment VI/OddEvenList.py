#Program to accept the numbers inside list and print Odd and Even Numbers.
(Even,Odd)=([],[])
for x in [int(input()) for i in range(int(input('Enter the numbers of Elements you want to enter and enter the respective numbers on next line: ')))]:
    if x %2==0:Even.append(x)
    else:Odd.append(x)
print(f"Even numbers: {Even}\nOdd numbers: {Odd}")