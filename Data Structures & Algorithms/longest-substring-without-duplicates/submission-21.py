class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        sSet = set()
        for j in range(len(s)):
            while s[j] in sSet:
                sSet.remove(s[i])
                i += 1

            sSet.add(s[j])
            longest = max(longest, j - i + 1)
        
        return longest
            