'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Problem Link: https://www.hackerrank.com/challenges/find-a-string/problem
'''

def count_substring(string, sub_string, count=0):
    f = string.find(sub_string)
    if (f != -1):
        count += 1
        count = count_substring(string[f + 1:], sub_string, count)
        return count
    else:
        return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)