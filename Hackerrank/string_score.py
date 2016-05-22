'''

Write an algorithm that takes a string as input and returns its "score" 
by converting each letter to its numeric form (e.g. a/A=1, b/B=2, c/C=3 etc.)

The input is a sentence, where spaces do not directly contribute to the score. 
A word's score is doubled for every adjacent pair of letters it contains (e.g. 
"rolled" contains a double "l" so the word score is multiplied by two).

Examples:

Input: A
Output: 1

Input: Now we only have one sentence
Output: 301

Input: The word needlessly contains two sets of double letters
Output: 1067

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
