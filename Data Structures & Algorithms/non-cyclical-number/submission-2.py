class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total
        
        slow = n
        fast = getNext(n)
        while slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        
        return True if fast == 1 else False