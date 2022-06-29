def longestPalindrome(s):
    res = ""
    def checkPalindrome(s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        temp = checkPalindrome(s,i,i)
        res = max(res,temp,key=len)
        temp = checkPalindrome(s,i,i+1)
        res = max(res,temp,key=len)
    return res

print(longestPalindrome("ccc"))
