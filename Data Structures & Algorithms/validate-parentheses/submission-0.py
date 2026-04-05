class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack & map
        stack = []
        mapping = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack == []:
            return True
        else:
            return False