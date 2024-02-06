'''
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Problem Link: https://www.hackerrank.com/challenges/the-minion-game/problem
'''

def minion_game(string):
    length = len(string)
    combinations =((length)*(length+1))/ 2
    score_Kevin,score_stuart = 0,0
    score_Kevin = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    score_stuart = combinations - score_Kevin

    if score_stuart == score_Kevin:print("Draw")
    elif score_stuart > score_Kevin:print("Stuart", int(score_stuart))
    else: print("Kevin", int(score_Kevin))

if __name__ == '__main__':
    s = input()
    minion_game(s)