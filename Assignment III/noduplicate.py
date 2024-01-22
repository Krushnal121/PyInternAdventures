#Approach 01
print(f"The list excluding duplicate values is as follows: {set([x for x in input('Approach 01: Enter the strings seperated by a space: ').split()])}")

#Approach 02
outputlist=[]
for x in [x for x in input("Approach 02: Enter the strings: ").split()]:
    if x not in outputlist:outputlist.append(x)
print(f"The list excluding duplicate values is as follows:{outputlist}")
