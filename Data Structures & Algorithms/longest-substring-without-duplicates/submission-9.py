class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        result = 0
        i = 0; j = 0
        while j < (len(s)):
            while s[j] in sSet:
                sSet.remove(s[i])
                i += 1
            result = max(result, j - i + 1)
            sSet.add(s[j])
            j += 1
        return result
