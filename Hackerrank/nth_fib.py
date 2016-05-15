'''

Function is given a number N as input and must return the 
Nth number of A, where A is the array where Nth element 
is the sum of (N-1)th and (N-2)th elements.

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
