class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        sSet = set(s)
        for char in s:
            i = 0; count = 0
            for j in range(len(s)):
                if s[j] == char:
                    count += 1        
                    
                while j - i + 1 - count > k:
                    if s[i] == char:
                        count -= 1
                    i += 1
                result = max(result, j - i + 1)
        return result