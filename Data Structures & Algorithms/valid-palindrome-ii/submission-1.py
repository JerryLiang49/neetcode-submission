class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def helper(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True


        while i < j:
            if s[i] != s[j]:
                return helper(s[i+1:j+1]) or helper(s[i:j])
            else:
                i += 1
                j -= 1
        return True
        
       