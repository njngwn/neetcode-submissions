class TimeMap:

    def __init__(self):
        # key: [(timestamp, value), (timestamp, value), ...]
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        key_map = self.timemap[key]
        left, right = 0, len(key_map)-1
        while left <= right:
            mid = left + (right-left)//2
            # print(f"left: {key_map[left][0]}, mid: {key_map[mid][0]}, right: {key_map[right][0]}")
            if key_map[mid][0] == timestamp:
                return key_map[mid][1]
            elif key_map[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return key_map[right][1] if right >= 0 else ""
