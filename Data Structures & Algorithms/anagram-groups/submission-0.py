class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # Use alphabet to determine whether each string is an anagram
        for word in strs:
            count = [0] * 26
            for char in word:
                # index is calculated from difference of ascii characers
                index = ord(char) - ord("a")
                count[index] += 1
            # Add word to dictionary
            key = tuple(count)
            result[key].append(word)
        return list(result.values())