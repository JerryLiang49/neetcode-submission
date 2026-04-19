class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        result = 0

        while queue:
            result += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for c in coins:
                    nxt = curr + c
                    if nxt == amount:
                        return result
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    queue.append(nxt)

        return -1