class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a frequency dictionary for the numbers in nunms
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # Create the frequency buckets
        freq = [[] for _ in range(len(nums) + 1)]
        # Place the items in the frequency buckets correspondingly
        for num, cnt in count.items():
            freq[cnt].append(num)
        result = []
        # traverse the frequency buckets in reverse order
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result