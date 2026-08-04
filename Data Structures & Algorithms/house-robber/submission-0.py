from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # at house i
        # 1. robbing the house -> go to i+2
        # 2. not robbing it -> go to i+1
        @lru_cache(maxsize=None)
        def findMaxAmount(i):
            if i >= len(nums):
                return 0
            return max(findMaxAmount(i+1), nums[i]+findMaxAmount(i+2))
        
        return findMaxAmount(0)
