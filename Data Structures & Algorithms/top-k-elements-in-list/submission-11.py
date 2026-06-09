class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        count = [[] for _ in range(len(nums) + 1)]
        result = []
        print(count)
        for num, frequency in freq.items():
            count[frequency].append(num)
        
        print(count)
        for i in range(len(count) - 1, -1, -1):
            for num in count[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
