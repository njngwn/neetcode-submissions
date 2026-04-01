from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(Counter(nums))