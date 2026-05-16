class Solution:
    def checkValidString(self, s: str) -> bool:
        pStack = []
        sStack = []

        for i, c in enumerate(s):
            if c == "(":
                pStack.append(i)
            elif c == "*":
                sStack.append(i)
            else:
                if not pStack and not sStack:
                    return False
                if pStack:
                    pStack.pop()
                else:
                    sStack.pop()
        
        while pStack and sStack:
            if pStack.pop() > sStack.pop():
                return False
            
        if pStack:
            return False
            
        return True
