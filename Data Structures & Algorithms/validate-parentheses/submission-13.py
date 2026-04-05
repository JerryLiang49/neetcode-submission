class Solution:
    def isValid(self, s: str) -> bool:
        match = {'}' : '{', ']' : '[', ")" : "("}
        stack = []

        for char in s:
            if char in match:
                if stack and match[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return stack == []