class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count.items():
            freq[frequency].append(num)
        print(freq)

        result = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                if len(result) == k:
                    return result