def uniquePaths(m,n):
    memo = {}
    def dp(m,n):
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        if (m,n) not in memo:
            memo[(m,n)] = dp(m-1, n) + dp(m,n-1)
        return memo[(m,n)]
    return dp(m,n)

print(uniquePaths([3,2]))