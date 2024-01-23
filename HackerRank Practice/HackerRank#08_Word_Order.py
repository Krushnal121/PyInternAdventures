'''
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

Input Format:
The first line contains the integer,n.
The next  lines each contain a word.

Output Format:
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Problem Link: https://www.hackerrank.com/challenges/word-order?isFullScreen=true
'''

strings=[input() for i in range(int(input()))]
string_repeatation={}
for string in strings:
    string_repeatation[string]=0
for string in strings:
    string_repeatation[string]+=1
print(len(string_repeatation))
for value in string_repeatation.values():print(value,end=" ")
