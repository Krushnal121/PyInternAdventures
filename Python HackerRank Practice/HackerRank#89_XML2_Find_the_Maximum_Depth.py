'''
You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as .
Input Format
The first line contains , the number of lines in the XML document.
The next  lines follow containing the XML document.

Output Format
Output a single line, the integer value of the maximum level of nesting in the XML document.

Problem Link: https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
'''

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth

    for child in elem:
        depth(child, level+1)
        maxdepth = max(maxdepth, level+2)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)