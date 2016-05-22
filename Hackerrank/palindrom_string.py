'''

Write a function which takes a string as a parameter and returns 1 
if that word is a palindrome, and 0 otherwise. A palindrom is a word 
which, when reversed, is the same as the original string e.g. "racecar".
If no string is entered, the algorigthm should return 0.

Examples
Input: door
Output: 0

Input: abba
Output: 1

Input: ""
Output: 0

'''

def palindrom_string(text):
    return 1 if text == text [::-1] else 0

