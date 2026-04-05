class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i = 0; j = len(heights) - 1
        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            result = max(result, area)
            smallerIndex = i if heights[i] < heights[j] else j
            if smallerIndex == i:
                i += 1
            else:
                j -= 1
        return result        