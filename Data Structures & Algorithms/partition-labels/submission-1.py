class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(list)
    
        for i, c in enumerate(s):
            d[c] = i

        start = 0
        last_index = 0
        result = []
        
        for i, c in enumerate(s):
            last_index = max(last_index, d[c])

            if last_index == i:
                result.append(i - start + 1)
                start = i + 1
            
        return result

        