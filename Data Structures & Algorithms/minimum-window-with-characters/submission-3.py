class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == "":
            return ""
        
        sDict = dict()
        tDict = dict()
        for c in t:
            tDict[c] = 1 + tDict.get(c, 0)

        result = [-1, -1]; resultLen = float("infinity")
        have = 0; need = len(tDict)
        i = 0
        for j in range(len(s)):
            char = s[j]
            sDict[char] = 1 + sDict.get(char, 0)
            if char in tDict and sDict[char] == tDict[char]:
                have += 1
            
            while have == need:
                if j - i + 1 < resultLen:
                    result = [i, j]
                    resultLen = j - i + 1
                
                sDict[s[i]] -= 1
                if s[i] in tDict and sDict[s[i]] < tDict[s[i]]:
                    have -= 1
                i += 1
        i, j = result
        if resultLen == float("infinity"): return ""
        else: return s[i:j+1]