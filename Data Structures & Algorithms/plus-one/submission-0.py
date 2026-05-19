class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        multiplier = 10 ** (length - 1)

        result = 0
        for digit in digits:
            result += digit * multiplier
            multiplier //= 10
        
        result += 1

        ans = []
        while result > 0:
            digit = result % 10
            ans.append(digit)
            result //= 10

        ans.reverse()
        
        return ans