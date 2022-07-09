def rotate_image(matrix):
    rows = len(matrix)
    matrix.reverse()
    for r in range(rows):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    return matrix

print(rotate_image([[1,2,3,2],[4,5,6,2],[7,8,9,2],[2,2,2,2]]))