class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        i = 0; j = len(height) - 1
        leftMax = height[i]; rightMax = height[j]
        # 2 pointers
        while i < j:
            # increment left if left height < right height
            # water stored = min(height[i], height[j]) - curr height
            if leftMax < rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                result += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                result += rightMax - height[j]
        return result