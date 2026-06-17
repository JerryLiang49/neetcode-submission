class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        self.group[freq].append(val)
        self.maxFreq = max(freq, self.maxFreq)

    def pop(self) -> int:
        element = self.group[self.maxFreq].pop()
        self.freq[element] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return element


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()