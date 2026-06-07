class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            result += strs[0][i]
            for s in strs:
                if result not in s:
                    return s[:i]
        
        return result