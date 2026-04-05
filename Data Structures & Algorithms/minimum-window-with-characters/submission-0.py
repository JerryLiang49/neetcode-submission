class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count = dict()
        window = dict()
        for c in t:
            count[c] = 1 + count.get(c, 0)

        have = 0; need = len(count)
        result = [-1, -1]; resultLen = float("infinity")
        i = 0
        for j in range(len(s)):
            c = s[j]
            window[c] = 1 + window.get(c, 0)

            if c in count and window[c] == count[c]:
                have += 1

            while have == need:
                if j - i + 1 < resultLen:
                    result = [i, j]
                    resultLen = j - i + 1
                
                window[s[i]] -= 1
                if s[i] in count and window[s[i]] < count[s[i]]:
                    have -= 1
                i += 1
        i, j = result
        if resultLen == float("infinity"):
            return ""
        else:
            return s[i:j+1]


        
        