class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def finish(weights, cap):
            finish = 0
            curr = 0
            for w in weights:
                curr += w
                if curr > cap:
                    finish += 1
                    curr = w
            return finish + 1


        l = max(weights)
        r = sum(weights)

        print(finish(weights, 7))
        
        result = 0
        while l <= r:
            mid = (l + r) // 2
            if finish(weights, mid) > days:
                l = mid + 1
            else:
                result = mid
                r = mid - 1
            
        return result