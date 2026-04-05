class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        leftBound = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftBound[i] = stack[-1]
            stack.append(i)

        stack = []
        rightBound = [len(heights)] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightBound[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(len(heights)):
            leftBound[i] += 1
            rightBound[i] -= 1
            maxArea = max(maxArea, heights[i] * (rightBound[i] - leftBound[i] + 1))
        return maxArea
