class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode with length and separator character
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        # Use 2 pointers
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # Get the length 
            length = int(s[i:j])
            # Extract the string
            string = s[j+1 : j+length+1]
            result.append(string)
            i = j+length+1  # Move to the next encoded string
        return result

