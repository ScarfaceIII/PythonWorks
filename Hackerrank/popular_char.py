'''
Write a function which accepts a string as a parameter and returns the character which 
appears most frequently.
If two or more characters are jointly the most common, the algorithm should return 
that which comes first in the alphabet. Only letters a-z need to be considered and 
you can rely only on lower case being used.

Example:

Input: blablab
Output: b

Input: abcdefghijklmnopqrstuvwyz
Output: a

Input: 'abracadabra'
Output: 'a'

'''

def popular_char(lst):
    # if ties were not considered it would have been a oneliner:
    # return max(set(input),key=input.count)
    lcounts = sorted([(i, input.count(i)) for i in set(input)], key=lambda x: x[1])
    count = max(lcounts, key=lambda x: x[1])[1]
    ties = filter(lambda x: x[1] == count, lcounts)
    return sorted(ties)[0][0]
