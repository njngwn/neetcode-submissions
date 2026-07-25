class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]] # starts with empty subset

        for num in nums:
            subset += [s + [num] for s in subset]

        return subset
