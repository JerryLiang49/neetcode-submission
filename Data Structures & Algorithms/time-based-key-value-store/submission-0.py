class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.map.get(key, [])
        l = 0; r = len(values) - 1
        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                l = m + 1
                result = values[m][0]
            else:
                r = m - 1
        return result

