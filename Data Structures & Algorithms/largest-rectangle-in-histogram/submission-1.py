class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                top = stack.pop()
                start = stack[-1] if stack else -1
                area = (i - start - 1) * heights[top] 
                max_area = max(area, max_area)

            stack.append(i)
        
        while stack:
            top = stack.pop()
            start = stack[-1] if stack else -1
            area = (len(heights) - start - 1) * heights[top] 
            max_area = max(area, max_area)

        return max_area