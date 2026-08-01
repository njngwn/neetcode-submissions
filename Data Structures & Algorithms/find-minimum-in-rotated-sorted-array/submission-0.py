class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            # print(f"left: {left}, right: {right}, mid: {mid}")
        
        return nums[left]


# 3,4,5,6,7,8,1,2
# left: 3, mid: 6, right: 2
# left > right and mid > right -> left = mid + 1
# left: 7, mid: 8, right: 2
# left > right and mid > right -> left = mid + 1
# left: 1, mid: 1, right: 2
# break -> left
# left < right and mid < right -> break 
# 7,8,1,2,3,4,5,6
# left: 7, mid: 2, right: 6
# left > right and mid < right -> left = mid + 1