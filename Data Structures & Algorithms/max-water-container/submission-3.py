class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        currMax = -1
        while i < j:
            curr = min(heights[i], heights[j]) * (j - i)
            currMax = max(curr, currMax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return currMax