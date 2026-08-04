from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        @lru_cache(maxsize=None)
        def calculateMaxAmount(i, isFirstRobbed):
            if i >= len(nums) or (isFirstRobbed and i == len(nums)-1):
                return 0

            return max(calculateMaxAmount(i+1, isFirstRobbed), nums[i]+calculateMaxAmount(i+2, isFirstRobbed))
        
        return max(calculateMaxAmount(0, True), calculateMaxAmount(1, False))