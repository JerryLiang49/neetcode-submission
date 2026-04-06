class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

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
            if index == len(digits):
                result.append("".join(path))
                return

            letters = mapping[digits[index]]
            for l in letters:
                path.append(l)
                dfs(index + 1, path)
                path.pop()

        dfs(0, [])
        return result