class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        # - nums[i] == nums[j] + nums[k]
        for i in range(0, len(nums)-2):
            target = -nums[i]
            left, right = i+1, len(nums)-1

            if i > 0 and nums[i] == nums[i-1]: continue

            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([-target, nums[left], nums[right]])

                    # remove duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return ans
