from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxFreq)
        frame = (maxFreq-1) * (n+1) + maxCount
        return max(frame, len(tasks))