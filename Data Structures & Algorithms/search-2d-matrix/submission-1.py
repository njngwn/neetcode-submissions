class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        top, bottom = 0, len(matrix)-1
        while top < bottom:
            mid = (top + bottom + 1) // 2
            # print(f"top: {top}, bottom: {bottom}, mid: {mid}, val: {matrix[mid][0]}")
            if matrix[mid][0] <= target:
                top = mid
            else:
                bottom = mid - 1
        
        # print(f"top: {top}, bottom: {bottom}")
        # print(matrix[top-1])
        # find in the col
        row = top
        left, right = 0, len(matrix[row])
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid

        return False