class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # sort 
        nums.sort()
        for i in range(len(nums)):
            j = i + 1; k = len(nums) - 1
            target = -nums[i]
            # check for duplicates on index i 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2 pointers
            while j < k:
                curr = nums[j] + nums[k]
                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # check for duplicates on index j
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return result


