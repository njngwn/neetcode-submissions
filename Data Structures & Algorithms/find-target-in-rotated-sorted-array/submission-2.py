class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the starting point
        def searchStartingPoint(nums: List[int]) -> int:
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
                
        # find the target using binary search
        def searchTarget(nums: List[int], target: int, left: int, right: int) -> int:
            # print("searchTarget")
            while left <= right:
                mid = (left + right) // 2
                # print(f"left: {nums[left]}, mid: {nums[mid]}, right: {nums[right]}")
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        start_point = searchStartingPoint(nums)
        target_index1 = searchTarget(nums, target, 0, start_point-1)
        target_index2 = searchTarget(nums, target, start_point, len(nums)-1)

        if target_index1 != -1:
            return target_index1
        elif target_index2 != -1:
            return target_index2
        else:
            return -1