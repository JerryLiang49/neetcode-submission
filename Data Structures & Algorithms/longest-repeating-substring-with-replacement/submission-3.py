class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sSet = set(s)
        longest = 0
        for char in sSet:
            count = 0
            i = 0
            for j in range(len(s)):
                if s[j] == char:
                    count += 1
                
                while j - i + 1 - count > k:
                    if s[i] == char:
                        count -= 1
                    i += 1
                
                longest = max(longest, j - i + 1)
        return longest

