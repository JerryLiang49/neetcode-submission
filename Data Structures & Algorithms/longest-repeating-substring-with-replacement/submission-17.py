class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        count = dict()
        
        maxFreq = 0
        longest = 0
        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)
            maxFreq = max(maxFreq, count[s[j]])

            while j - i + 1 - maxFreq > k:
                count[s[i]] -= 1
                i += 1
            longest = max(longest, j - i + 1)        
        return longest