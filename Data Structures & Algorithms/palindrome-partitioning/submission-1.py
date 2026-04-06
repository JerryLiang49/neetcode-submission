class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(word):
            return word == word[::-1]

        def dfs(index, path):
            if index == len(s):
                result.append(path[:])
                return
                
            for i in range(index + 1, len(s) + 1):
                string = s[index:i]
                if is_palindrome(string):
                    path.append(string)
                    dfs(i, path)
                    path.pop()
                
        dfs(0, [])
        return result

