class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        result = 0
        while i < j:
            height = min(heights[i], heights[j])
            currArea = (j - i) * height
            result = max(result, currArea)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return result