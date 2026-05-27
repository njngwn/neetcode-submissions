class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # edge case
        if len(nums) < 4: return []

        nums.sort()
        ans = []

        # fix nums[a] and nums[b]
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]: continue # remove duplicates

            for b in range(a+1, len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]: continue # remove duplicates

                new_target = target - nums[a] - nums[b]
                c, d = b+1, len(nums)-1
                while c < d:
                    if nums[c] + nums[d] == new_target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        
                        # remove duplicates
                        while c < d and nums[c] == nums[c+1]: c += 1
                        while c < d and nums[d] == nums[d-1]: d -= 1

                        c += 1
                        d -= 1

                    elif nums[c] + nums[d] < new_target:
                        c += 1
                    else:
                        d -= 1

        return ans