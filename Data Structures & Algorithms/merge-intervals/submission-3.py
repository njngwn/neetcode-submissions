class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        intervals.sort(key=lambda x: x[0])

        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            i += 1
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1
            res.append([start, end])
        
        return res
