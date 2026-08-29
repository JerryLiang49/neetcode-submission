class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def dfs(i, path):
            if i == len(digits):
                result.append(path[:])
                return
            
            choices = mapping[digits[i]]
            for c in choices:
                path += c
                dfs(i + 1, path)
                path = path[:-1]
        
        if digits:
            dfs(0, "")
        return result