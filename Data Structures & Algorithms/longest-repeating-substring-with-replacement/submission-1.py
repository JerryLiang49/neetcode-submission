class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)  # Get all unique characters in the string

        for c in charSet:  # Try making the whole window consist of character c
            count = 0       # Count = how many times c appears in current window
            l = 0           # Left pointer of sliding window
            for r in range(len(s)):  # Right pointer of sliding window
                if s[r] == c:
                    count += 1

                # If more than k characters need to be replaced
                # window size = (r - l + 1)
                # if (window size - count of c) > k, it's invalid
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1  # Shrink the window from the left
                    l += 1
                    
                # Update the result with the max valid window size
                res = max(res, r - l + 1)
                
        return res