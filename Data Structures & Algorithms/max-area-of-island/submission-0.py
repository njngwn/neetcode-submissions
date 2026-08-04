class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int, area: int) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return area
            
            grid[r][c] = 0
            area += 1

            for dr, dc in directions:
                area = dfs(r+dr, c+dc, area)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c, 0))
            
        return max_area