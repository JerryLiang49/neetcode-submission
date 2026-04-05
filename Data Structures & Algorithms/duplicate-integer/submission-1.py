class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sSet = set()
        for num in nums:
            if num in sSet:
                return True
            else:
                sSet.add(num)
        return False