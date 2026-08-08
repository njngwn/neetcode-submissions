class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert all stones to negative and build a heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first-second)
            
        heapq.heappush(stones, 0)
        return abs(stones[0])

