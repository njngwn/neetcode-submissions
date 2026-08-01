class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        while low < high:
            mid = low + (high-low)//2
            total_day = 1
            weight_per_day = 0
            # print("---------------------------")
            # print(f"weight capacity: {mid}")
            # print("---------------------------")
            for weight in weights:
                weight_per_day += weight
                if weight_per_day > mid:
                    total_day += 1  # change to next day
                    weight_per_day = weight

                # print(f"day: {total_day}, weight: {weight_per_day}, {weight_per_day > mid}")
                
                if total_day > days:
                    break
            
            if total_day <= days:
                high = mid
            else:
                low = mid + 1

        return low