class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = dict()
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        def dfs(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    dfs(path)

                    path.pop()
                    count[num] += 1
        
        dfs([])
        return result
