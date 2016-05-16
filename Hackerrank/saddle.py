'''
Given a list of numbers that represents a square matrix, 
function must return the saddle point of the matrix 
(namely, the minimum value in a row, who is also the 
maximum in its column).

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

