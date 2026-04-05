class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = dict()
        for num in nums:
            numsDict[num] = 1 + numsDict.get(num, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, frequency in numsDict.items():
            freq[frequency].append(num)
        print(freq)

        result = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
                