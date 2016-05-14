'''
Find the most popular character in a given string.

Example input: 'abracadabra'
Example output: 'a'

'''

def popular_char(lst):
    return max(set(lst),key=lst.count)

