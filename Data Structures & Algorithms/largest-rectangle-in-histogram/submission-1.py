class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        largest = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackIndex, stackHeight = stack.pop()
                largest = max(largest, stackHeight * (i - stackIndex))
                start = stackIndex
            stack.append((start, h))
        
        for i, h in stack:
            largest = max(largest, h * (len(heights)- i))
        return largest