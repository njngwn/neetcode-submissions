import bisect
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        key_map = self.timemap[key]
        idx = bisect.bisect_right(key_map, (timestamp, chr(127)))

        if idx == 0:
            return ""
        else:
            return key_map[idx-1][1]