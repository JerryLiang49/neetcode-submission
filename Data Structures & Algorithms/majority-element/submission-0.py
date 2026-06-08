class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        count = 0

        for num in nums:
            if count == 0:
                answer = num
            if answer == num:
                count += 1
            else:
                count -= 1
        
        return answer