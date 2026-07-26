class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def dfs(index, path):
            if index == len(s):
                result.append(" ".join(path))
                return
            
            for i in range(index, len(s)):
                if s[index:i + 1] in wordDict:
                    path.append(s[index:i + 1])
                    dfs(i + 1, path)

                    path.pop()

        dfs(0, [])
        return result