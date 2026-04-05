class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [] #(index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largest = max(largest, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))
        
        return largest

        