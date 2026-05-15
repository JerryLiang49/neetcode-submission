class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        d = Counter(hand)

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

