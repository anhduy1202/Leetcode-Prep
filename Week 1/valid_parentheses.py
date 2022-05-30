from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                top = stack[-1]
                if char == ')' and top == '(':
                    stack.pop()
                elif char == ']' and top == '[':
                    stack.pop()
                elif char == '}' and top == '{':
                    stack.pop()
                else:
                    stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False
