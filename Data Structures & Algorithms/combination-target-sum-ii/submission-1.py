class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(index, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if remaining < 0:
                    continue
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                dfs(i + 1, path, remaining - candidates[i])
                path.pop()
            
        dfs(0, [], target)
        return result