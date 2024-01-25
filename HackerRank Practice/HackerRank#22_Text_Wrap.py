import textwrap

def wrap(string, max_width):
    outstr="\n".join(textwrap.TextWrapper(width=max_width).wrap(text=string))
    return outstr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)