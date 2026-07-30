class Solution:
    # brute force
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for start, height in enumerate(heights):
            min_height = height
            for end in range(start, len(heights)):
                min_height = min(min_height, heights[end])
                area = (end-start+1) * min_height
                max_area = max(max_area, area)

        return max_area