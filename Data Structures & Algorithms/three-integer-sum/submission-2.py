class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue

            pivot = nums[i]
            if pivot > 0: break

            left, right = i+1, len(nums)-1
            while left < right:
                total = pivot + nums[left] + nums[right]
                if left < right and total == 0:
                    triplets.append([pivot, nums[left], nums[right]])

                    # remove duplicates
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1

                    left, right = left + 1, right - 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets