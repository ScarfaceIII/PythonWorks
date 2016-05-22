'''

A Saddle point in an array is a number that is larger than or equal 
to every number in its column and, at the same time, smaller than or 
equal to every number in its row.

Write a function which takes a string representing a square array 
of integers (read left to right, top to bottom) as a parameter and 
returns the number of saddle points, if any, in the array.

Examples:

Input 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

Output: 1 (saddle point is 13)

'''

def saddle(input):
    arr = input.split(' ')
    n = int(pow(len(arr),.5))
    matrix = [[0 for x in range(n)] for y in range(n)]

    for i in xrange(n):
        for j in xrange(n):
            matrix[i][j] = int(arr[j+(n*i)])
    print matrix    
    colMax = [float('-inf')] * n
    rowMin = [float('inf')] * n 
    for i in xrange(n):
        for j in xrange(n):
            rowMin[i] = min(rowMin[i], matrix[i][j])
            colMax[j] = max(colMax[j], matrix[i][j])
    
    saddle_points = 0
    for i in xrange(n):
        for j in xrange(n):
            if matrix[i][j] == rowMin[i] == colMax[j]:
                saddle_points += 1
    return saddle_points

