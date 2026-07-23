class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        if sum(matchsticks) % 4:
            return False
        
        target = sum(matchsticks) // 4

        def dfs(index):
            if index == len(matchsticks):
                return True

            for i in range(len(sides)):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True

                    sides[i] -= matchsticks[index]
                
            return False

        return dfs(0)

            
