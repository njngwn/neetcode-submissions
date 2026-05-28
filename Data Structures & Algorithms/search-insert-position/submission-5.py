class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high, mid = 0, len(nums)-1, len(nums)//2

        if target < nums[low]: return low
        if target > nums[high]: return len(nums)

        while low <= high:
            mid = (low + high)//2
            print(nums[mid])
            if nums[mid] == target: return mid
            elif nums[mid] > target: high = mid-1
            else: low = mid+1
        
        return low
