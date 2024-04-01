'''
You are given an HTML code snippet of  lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:

Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2

Problem link: https://www.hackerrank.com/challenges/html-parser-part-1/problem
'''

from html.parser import HTMLParser

N = int(input())


class MyHTMLParser(HTMLParser):  # Subclass

    def handle_starttag(self, tag, attributes):
        print('Start :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attributes):
        print('Empty :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])


Parser = MyHTMLParser()
Parser.feed(''.join([input().strip() for i in range(0, N)]))