class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p,s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)

        stack = []
        for p, s in ps:
            reach = (target - p) / s
            if not stack or stack[-1] < reach:
                stack.append(reach)
        
        return len(stack)