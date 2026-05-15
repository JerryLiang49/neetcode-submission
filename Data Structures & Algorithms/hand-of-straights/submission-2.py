class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        d = Counter(hand)

        for num in hand:
            start = num
            while start - 1 in d:
                start -= 1
            while start <= num:
                while d[start]:
                    for i in range(start, start + groupSize):
                        if not d[i]:
                            return False
                        d[i] -= 1
                start += 1
        
        return True

