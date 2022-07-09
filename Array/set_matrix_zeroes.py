from copy import deepcopy


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        first_col_has_zeroes = False
        first_row_has_zeroes = False
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_has_zeroes = True
                    if c == 0:
                        first_col_has_zeroes = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0 

        if first_row_has_zeroes:
            for c in range(columns):
                matrix[0][c] = 0

        if first_col_has_zeroes:
            for r in range(rows):
                matrix[r][0] = 0
        return matrix


solution = Solution()
print(solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
