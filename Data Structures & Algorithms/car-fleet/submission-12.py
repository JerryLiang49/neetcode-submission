class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)
        print(ps)
        stack = []
        for pos, speed in ps:
            time = (target - pos) / speed
            print(time)
            if not stack or time > stack[-1]:
                stack.append(time)
            print(stack)

        return len(stack)