class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        target = self.d[key]
        result = ""

        l = 0
        r = len(target) - 1
        while l <= r:
            mid = (l + r) // 2
            if target[mid][1] > timestamp:
                r = mid - 1
            elif target[mid][1] < timestamp:
                result = target[mid][0]
                l = mid + 1
            else:
                return target[mid][0]
            
        return result