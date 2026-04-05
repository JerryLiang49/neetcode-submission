class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        j = 0
        longest = 0
        sset = set()
        while j < len(s):
            while s[j] in sset:

                sset.remove(s[i])
                i += 1
            longest = max(longest, j - i + 1)
            sset.add(s[j])
            j += 1
        return longest