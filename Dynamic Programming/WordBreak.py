from collections import deque

def wordBreak(s, wordDict):
    cache = [False] * (len(s) + 1)
    cache[len(s)] = True
    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            # len(s[i:]) >= len(w)
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                cache[i] = cache[i + len(w)]
            if cache[i]:
                break
    return cache[0]


def wordBreakBFS(s, wordDict):
    q = deque([s])
    seen = set()
    while q:
        s = q.popleft()  
        for word in wordDict:
            if s.startswith(word):
                new_s = s[len(word):]
                if new_s == "":
                    return True
                if new_s not in seen:
                    q.append(new_s)
                    seen.add(new_s)
    return False

print(wordBreakBFS("catsandog",["cats","dog","sand","and","cat"]))
