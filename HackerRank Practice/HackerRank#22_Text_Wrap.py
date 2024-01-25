import textwrap
lst1=[]
lst2=[]
def wrap(string, max_width):
    length = len(string)
    lst1=[string[i] for i in range(length)]
    for i in range (0,length,max_width):
        if (i+max_width)!=length:
            lst2.append(string[i:i+4])
            lst2.append("\n")
        else:
            lst2.append(string[i:])
    if lst2[-1]=="\n":lst2.pop()
    lststr="".join(lst2)
    return lststr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)