class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}   # {num:i}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen.get(difference), i]
            seen[num] = i
        
        return None