class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        i = 0
        for j in range(len(nums)):
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            if i > q[0]:
                q.popleft()
            
            if j + 1 >= k:
                result.append(nums[q[0]])
                i += 1
        return result