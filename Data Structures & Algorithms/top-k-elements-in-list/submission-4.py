class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        result = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = [[] for _ in range(len(nums) + 1)]
        for i, n in count.items():
            freq[n].append(i)
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(result) == k:
                    return result
                result.append(num)
        return result