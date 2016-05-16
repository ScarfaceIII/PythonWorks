'''
Given a string, function must return its score.
Each letter's score is the letter's position in the 
alphabet (spaces or symbols don't count).
If the string has two consecutive letters, score duplicates.

'''

def letter_val(letter):
    return  ord(letter.lower()) - ord('a') + 1 if letter.isalpha() else 0

def string_score( input):
    words = input.split(' ')
    tot_score = 0
    for word in words:
        score = letter_val(word[0])
        multiplier = 1
        for i in xrange(1,len(word)):
            score += letter_val(word[i])
            if word[i] == word[i-1]:
                multiplier = multiplier * 2
        tot_score += score * multiplier 
    return tot_score
