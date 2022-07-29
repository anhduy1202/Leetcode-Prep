from collections import Counter


def find_permutation(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = Counter(pattern)

    # our goal is to match all the characters from the 'char_frequency' with the current
    # window try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def permuate(s1, s2):
    k = len(s1)
    d1 = Counter(s1)

    # initial window
    window = s2[:k]
    d2 = Counter(window)

    # check the intial window
    if d1 == d2:
        return True

    for i in range(len(s2)-k):

        # SLIDE THE WINDOW
        # 1 - remove s2[i]
        if d2[s2[i]] == 1:
            del d2[s2[i]]
        elif d2[s2[i]] > 1:
            d2[s2[i]] -= 1

        # 2- add s2[i+k]
        if s2[i+k] in d2:
            d2[s2[i+k]] += 1
        else:
            d2[s2[i+k]] = 1

        # check after sliding
        if d1 == d2:
            return True

    return False


print(find_permutation(
    "abac", "abc"))
