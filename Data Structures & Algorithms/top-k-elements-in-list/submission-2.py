class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = [[] for _ in range(len(nums) + 1)]
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        for i, n in count.items():
            freq[n].append(i)
        print(freq)
        for i in range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                print(len(result))
                if len(result) == k:
                    return result
                result.append(freq[i][j])
        return result