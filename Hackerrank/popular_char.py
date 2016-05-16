'''
Find the most popular character in a given string.

Example input: 'abracadabra'
Example output: 'a'

'''

def popular_char(lst):
    # if ties were not considered it would have been a oneliner:
    # return max(set(input),key=input.count)
    lcounts = sorted([(i, input.count(i)) for i in set(input)], key=lambda x: x[1])
    count = max(lcounts, key=lambda x: x[1])[1]
    ties = filter(lambda x: x[1] == count, lcounts)
    return sorted(ties)[0][0]
