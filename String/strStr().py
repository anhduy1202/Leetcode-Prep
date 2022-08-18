def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    start2 = 0
    end = 0
    res = -1
    for start in range(len(haystack)):
        while haystack[end] == needle[start2]:
            if (end-start)+1 == len(needle):
                res = start
                break
            else:
                end += 1
                start2 += 1
        start2 = 0
        end+=1
    return res

print(strStr("hello","ll"))