class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        frequency = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            frequency[freq].append(num)
        
        result = []
        for i in range(len(frequency) - 1, -1, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
