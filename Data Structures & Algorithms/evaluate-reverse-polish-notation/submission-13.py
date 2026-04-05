class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t == "-":
                a = int(stack.pop())
                stack.append(int(stack.pop()) - a)
            elif t == "/":
                a = int(stack.pop())
                stack.append(int(float(stack.pop())) / a)
            else:
                stack.append(t)
        return int(stack[-1])