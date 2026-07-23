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
        
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            choices = mapping[digits[index]]
            for c in choices:
                path += c
                dfs(index + 1, path)
                path = path[:-1]

        if digits:    
            dfs(0, "")
        return result