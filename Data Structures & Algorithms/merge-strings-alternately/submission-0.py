class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        
        shorter = min(len(word1), len(word2))
        result = ""

        while i < shorter:
            result += word1[i]
            i += 1
            result += word2[j]
            j += 1
        
        while i < len(word1):
            result += word1[i]
            i += 1
        
        while j < len(word2):
            result += word2[j]
            j += 1
        
        return result