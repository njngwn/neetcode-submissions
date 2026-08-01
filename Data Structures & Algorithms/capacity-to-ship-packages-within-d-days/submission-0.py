class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        for i in range(low, high+1):
            total_day = 1
            weight_per_day = 0
            # print("---------------------------")
            # print(f"weight capacity: {i}")
            # print("---------------------------")
            for weight in weights:
                weight_per_day += weight
                # print(f"day: {total_day}, weight: {weight_per_day}")
                if weight_per_day > i:
                    total_day += 1  # change to next day
                    weight_per_day = weight
                
                if total_day > days:
                    break
            
            if total_day <= days:
                return i
        
        return -1