class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def threeSum(nums, target):
            nums.sort()
            result = []

            for i in range(len(nums)):

                if i > 0 and nums[i] == nums[i-1]:
                    continue

                j = i + 1
                k = len(nums) - 1
                while j < k:
                    curr = nums[i] + nums[j] + nums[k]
                    if curr < target:
                        j += 1
                    elif curr > target:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1

                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
            
            return result

        nums.sort()
        result = []

        for i in range(len(nums)):
            find = target - nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            sub_results = threeSum(nums[i + 1:], find)

            for triplet in sub_results:
                result.append([nums[i]] + triplet)
        
        return result

        