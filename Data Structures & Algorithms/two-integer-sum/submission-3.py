class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in pair_map and pair_map[diff] != i:
                return [pair_map[diff], i]
            pair_map[n] = i

        return []