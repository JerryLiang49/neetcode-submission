class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        curr_sum = 0
        result = 0

        for num in nums:
            curr_sum += num
            if curr_sum == k:
                result += 1
            if curr_sum - k in d:
                result += d[curr_sum - k]
            d[curr_sum] += 1
        print(d)

        return result

