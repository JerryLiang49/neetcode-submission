class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = dict()
        for num in hand:
            d[num] = d.get(num, 0) + 1

        hand.sort()

        for i in range(len(hand)):
            if d[hand[i]]:
                group = [hand[i]]
                d[hand[i]] -= 1
                for i in range(groupSize - 1):
                    if group[-1] + 1 in d:
                        d[group[-1] + 1] -= 1
                        group.append(group[-1] + 1)
                    else:
                        return False
        
        return True

