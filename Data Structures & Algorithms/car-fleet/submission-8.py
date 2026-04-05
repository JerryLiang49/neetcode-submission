class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)
        stack = []
        for pos, speed in ps:
            time = (target - pos)/speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)