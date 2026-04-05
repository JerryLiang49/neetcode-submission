class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = dict()
        sDict = dict()

        for c in t:
            tDict[c] = 1 + tDict.get(c, 0)
        
        have = 0
        need = len(tDict)
        result = [-1, -1]
        length = float("infinity")
        i = 0
        for j in range(len(s)):
            sDict[s[j]] = 1 + sDict.get(s[j], 0)
            if s[j] in tDict and sDict[s[j]] == tDict[s[j]]:
                have += 1
            
            while have == need:
                if j - i + 1 < length:
                    length = j - i + 1
                    result = [i, j]
                
                sDict[s[i]] -= 1
                if s[i] in tDict and sDict[s[i]] < tDict[s[i]]:
                    have -= 1
                i += 1
            
        i, j = result
        if length == float("infinity"): return ""
        return s[i:j+1]