'''
Given a string, function must return its score.
Each letter's score is the letter's position in the 
alphabet (spaces or symbols don't count).
If the string has two consecutive letters, score duplicates.

'''

def letter_val(letter):
    return  ord(letter.lower()) - ord('a') + 1 if letter.isalpha() else 0

def string_score(string):
    score = letter_val(string[0])
    for i in xrange(1,len(string)):
        score += letter_val(string[i])
        if string[i] == string[i-1]:
            score = score * 2
    return score
