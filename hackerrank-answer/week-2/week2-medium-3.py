# https://www.hackerrank.com/challenges/the-minion-game
# The minion game

def determine_winner(string):
    length = len(string)
    vowels = 'AEIOU'
    points = 0
    points2 = 0
    for i in range(length):
        if string[i] in vowels:
            points += sub_add(length, i)

    for i in range(length):
        if string[i] not in vowels:
            points2 += sub_add(length, i)

    if points > points2:
        print 'Kevin', points
    elif points2 > points:
        print 'Stuart', points2
    else:
        print('Draw')

def sub_add(start, stop):
    return start - stop


determine_winner(raw_input())
