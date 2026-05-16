class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(list)
    
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                d[c] = i
            
        l = -1
        last_index = 0
        result = []
        
        for i in range(len(s)):
            last_index = max(last_index, d[s[i]])
            if last_index == i:
                result.append(i - l)
                last_index = i
                l = i
            
        return result

        