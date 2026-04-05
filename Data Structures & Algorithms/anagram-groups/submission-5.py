class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        freqDict = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                index = ord('a') - ord(c)
                count[index] += 1
            freqDict[tuple(count)].append(word)
            print(freqDict)
        return list(freqDict.values())

        