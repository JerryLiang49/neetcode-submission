class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            print(s[i], s[j])
            if s[i] == " " or not s[i].isalnum():
                i += 1
            elif s[j] == " " or not s[j].isalnum():
                j -= 1 
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True