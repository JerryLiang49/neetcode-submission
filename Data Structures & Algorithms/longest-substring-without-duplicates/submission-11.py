class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        ans = 0
        sSet = set()
        for j in range(len(s)):
            if s[j] not in sSet:
                sSet.add(s[j])
            else:
                while s[j] in sSet:
                    sSet.remove(s[i])
                    i += 1
                sSet.add(s[j])
            ans = max(ans, j - i + 1)
        
        return ans
