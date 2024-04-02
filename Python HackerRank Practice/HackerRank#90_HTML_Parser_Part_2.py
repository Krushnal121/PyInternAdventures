'''
You are given an HTML code snippet of  lines.
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:

>>> Single-line Comment
Comment
>>> Data
My Data
>>> Multi-line Comment
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:
Note: Do not print data if data == '\n'.

Problem Link : https://www.hackerrank.com/challenges/html-parser-part-2/problem
'''

from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


if __name__ == '__main__':
    parser = CustomHTMLParser()

    n = int(input())

    html_string = ''
    for i in range(n):
        html_string += input().rstrip() + '\n'

    parser.feed(html_string)
    parser.close()