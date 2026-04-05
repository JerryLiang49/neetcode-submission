class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # Use alphabet to determine whether each string is an anagram
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord('a') - ord(c)
                count[index] += 1
                # index is calculated from difference of ascii characers
            result[tuple(count)].append(s)
            # Add word to dictionary
        return list(result.values())