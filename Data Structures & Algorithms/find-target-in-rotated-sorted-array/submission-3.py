class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the min element
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        start_point = left
        
        # find the interval where the target exists
        if target >= nums[start_point] and target <= nums[-1]:
            left, right = start_point, len(nums)-1
        else:
            left, right = 0, start_point-1
        
        # binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1