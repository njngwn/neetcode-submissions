class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        top, bottom = 0, len(matrix)
        while top < bottom:
            mid = (top + bottom) // 2
            # print(f"top: {top}, bottom: {bottom}, mid: {mid}, val: {matrix[mid][0]}")
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bottom = mid
        
        # print(f"top: {top}, bottom: {bottom}")
        # print(matrix[top-1])
        # find in the col
        left, right = 0, len(matrix[top-1])
        while left < right:
            mid = (left + right) // 2
            if matrix[top-1][mid] == target:
                return True
            elif matrix[top-1][mid] < target:
                left = mid + 1
            else:
                right = mid

        return False