class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sDict = dict()
        tDict = dict()

        for char in t:
            tDict[char] = 1 + tDict.get(char, 0)
        
        result = [-1, -1]
        resultLen = float("infinity")
        i = 0
        need = len(tDict)
        have = 0
        for j in range(len(s)):
            sDict[s[j]] = 1 + sDict.get(s[j], 0)
            if s[j] in tDict and sDict[s[j]] == tDict[s[j]]:
                have += 1
            
            while need == have:
                if j - i + 1 < resultLen:
                    result = i, j
                    resultLen = j - i + 1

                sDict[s[i]] -= 1
                if s[i] in tDict and sDict[s[i]] < tDict[s[i]]:
                    have -= 1
                i += 1
        
        i, j = result
        if resultLen == float("infinity"):
            return ""
        return s[i:j+1]