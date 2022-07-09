import re
def reverseWord(s):
    s = ' ' + s # left pad
    n = len(s)
    ret = ""; prev = n
    for i in range(n-1, -1, -1):
        if s[i] != ' ': continue
        # found delim
        ret += s[i:prev]
        prev = i
    return re.sub(' +', ' ', ret.strip())


print(reverseWord("  hello world  "))