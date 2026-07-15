class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in lookup and stack:
                if stack[-1] == lookup[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0