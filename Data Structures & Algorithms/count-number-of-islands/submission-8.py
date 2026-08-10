class Solution:
    def dfs(self, grid, r, c, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 
        if grid[r][c] == "0":
            return 
        grid[r][c] = "0"
        self.dfs(grid, r - 1, c, rows, cols)
        self.dfs(grid, r + 1, c, rows, cols)
        self.dfs(grid, r, c - 1, rows, cols)
        self.dfs(grid, r, c + 1, rows, cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0]),
        res = 0
        if not grid:
            return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    self.dfs(grid, r, c, rows, cols)
        return res