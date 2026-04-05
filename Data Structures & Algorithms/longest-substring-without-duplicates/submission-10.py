class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        longest = 0
        i = 0; j = 0
        while j < len(s):
            while s[j] in sSet:
                sSet.remove(s[i])
                i += 1
            longest = max(longest, j - i + 1)
            sSet.add(s[j])
            j += 1
        return longest
