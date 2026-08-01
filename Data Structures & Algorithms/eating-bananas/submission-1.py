import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        # binary search
        while low < high:
            mid = (low + high) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)
                # print(f"pile: {pile}, hour: {hour}")
            
            # print(f"low: {low}, high: {high}, mid: {mid}, total hour: {hour}")
            if hour <= h:
                high = mid
            else:
                low = mid + 1

        return low
