class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        i = 0; j = len(height) - 1
        leftMax = height[i]; rightMax = height[j]
        result = 0
        while i < j:
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                result += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                result += rightMax - height[j]
        return result