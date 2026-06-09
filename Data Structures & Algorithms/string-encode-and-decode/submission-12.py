class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                result.append(s[j+1:j+1+length])
                j = j + 1 + length
                i = j
            j += 1

        return result
