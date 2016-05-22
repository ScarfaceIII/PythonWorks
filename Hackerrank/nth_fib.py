'''

Let `A` be an integer sequence for which the Nth number is 
defined as the summation of its two previous numbers, i.e. the (N-1) and (N-2).

Write a function that takes an integer N, between 0 and 10, and returns the 
Nth member of this sequence, given that the first two numbers of this sequence 
are 0 and 1 respectively.

Examples:

Input: 1
Output: 0

Input: 3
Output: 2

'''
def ifibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def nth_fib(N):
    fibs = [fib for fib in ifibonacci(N)]
    return fibs[-1]
