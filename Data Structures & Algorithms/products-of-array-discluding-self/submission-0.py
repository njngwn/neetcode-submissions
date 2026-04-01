class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # [1, 2, 8, 48]
        # [48, 48, 24, 6]
        product_left = [nums[0]] * len(nums)
        product_right = [nums[len(nums)-1]] * len(nums)
        product = []

        # calculate product from left until own index
        for i in range(1, len(nums)):
            product_left[i] = product_left[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            product_right[i] = product_right[i+1] * nums[i]

        for i in range(len(nums)):
            val1 = product_left[i-1] if i > 0 else 1
            val2 = product_right[i+1] if i < len(product_right)-1 else 1
            product.append(val1 * val2)
        
        return product
