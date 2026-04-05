class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0; j = 0
        result = []
        q = deque() # queue of the indexes; the index of the largest number is at the top
        while j < len(nums):
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)

            if i > q[0]:
                q.popleft()
            
            if j + 1 >= k:
                result.append(nums[q[0]])
                i += 1
            j += 1
        return result

        