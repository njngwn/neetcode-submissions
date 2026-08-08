class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            heapq.heappush(dist, (x**2+y**2, x, y))
        
        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(dist)
            res.append([x, y])

        return res