class TimeMap:

    def __init__(self):
        self.kvs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvs[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        target = self.kvs[key]
        l = 0
        r = len(target) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if target[mid][1] <= timestamp:
                l = mid + 1
                result = target[mid][0]
            else:
                r = mid - 1
        return result