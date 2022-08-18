def rotateImage(matrix):
    list.reverse(matrix)
    rows = len(matrix)
    for row in range(rows):
        for c in range(row):
            matrix[row][c],matrix[c][row] = matrix[c][row], matrix[row][c]
    return matrix

print(rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))