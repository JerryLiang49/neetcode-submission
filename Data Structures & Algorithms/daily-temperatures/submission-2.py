class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((t, i))
        return result