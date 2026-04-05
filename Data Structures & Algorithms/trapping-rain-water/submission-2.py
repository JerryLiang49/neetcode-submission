class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        i = 0; j = len(height) - 1
        leftMax = height[i]; rightMax = height[j]
        while i < j:
            if leftMax < rightMax:
                i += 1
                leftMax = max(height[i], leftMax)
                result += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(height[j], rightMax)
                result += rightMax - height[j]
        return result 