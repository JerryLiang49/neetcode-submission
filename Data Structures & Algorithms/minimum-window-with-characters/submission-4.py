class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCount = dict()
        tCount = dict()

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        have = 0; need = len(tCount)
        result = [-1, -1]; resultLen = float("infinity")
        i = 0
        for j in range(len(s)):
            char = s[j]
            sCount[char] = 1 + sCount.get(char, 0)
            if char in tCount and sCount[char] == tCount[char]:
                have += 1
            
            while have == need:
                if j - i + 1 < resultLen:
                    resultLen = j - i + 1
                    result = [i, j]
                
                sCount[s[i]] -= 1
                if s[i] in tCount and sCount[s[i]] < tCount[s[i]]:
                    have -= 1
                i += 1
            
        i, j = result
        if resultLen == float("infinity"): return ""
        else: return s[i:j+1]
                
