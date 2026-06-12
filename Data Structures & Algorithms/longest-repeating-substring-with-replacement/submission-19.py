class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        d = defaultdict(int)
        longest = 0
        maxFreq = 0

        for j in range(len(s)):
            d[s[j]] += 1
            maxFreq = max(maxFreq, d[s[j]])

            while j - i + 1 - maxFreq > k:
                d[s[i]] -= 1
                maxFreq = max(maxFreq, d[s[j]])
                i += 1
            
            longest = max(longest, j - i + 1)
        
        return longest





