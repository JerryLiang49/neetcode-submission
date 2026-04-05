class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = dict()
        sDict = dict()
        for char in t:
            tDict[char] = 1 + tDict.get(char, 0)

        have = 0
        need = len(tDict)
        result = [-1, -1]
        length = float('inf')
        i = 0
        for j in range(len(s)):
            char = s[j]
            sDict[char] = 1 + sDict.get(char, 0)
            if char in tDict and sDict[char] == tDict[char]:
                have += 1

            while have == need:
                if j - i + 1 < length:
                    result = [i, j]
                length = min(j - i + 1, length)
                
                sDict[s[i]] -= 1
                if s[i] in tDict and sDict[s[i]] < tDict[s[i]]:
                    have -= 1
                i += 1
        
        i, j = result
        return s[i:j+1]

