class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        wordDict = set(wordDict)
        cache = dict()

        def dfs(index):
            if index == len(s):
                return [""]
            if index in cache:
                return cache[index]

            result = []
            for i in range(index, len(s)):
                word = s[index:i + 1]
                if word not in wordDict:
                    continue
                strings = dfs(i + 1)
                for substr in strings:
                    sentence = word
                    if substr:
                        sentence += " " + substr
                    result.append(sentence)
            cache[index] = result
            return result

        return dfs(0)