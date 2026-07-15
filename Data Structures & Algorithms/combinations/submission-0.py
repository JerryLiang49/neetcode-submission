class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(path, index):
            if len(path) == k:
                result.append(path.copy())
                return
            
            for i in range(index, n + 1):
                path.append(i)
                dfs(path, i + 1)

                path.pop()
            
        dfs([], 1)
        return result