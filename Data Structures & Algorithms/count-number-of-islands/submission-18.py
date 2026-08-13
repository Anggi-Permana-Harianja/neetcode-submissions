class Solution:
    def dfs(self, r, c):
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return 
        if self.grid[r][c] == "0":
            return 
        self.grid[r][c] = "0"
        self.dfs(r - 1, c)
        self.dfs(r + 1, c)
        self.dfs(r, c - 1)
        self.dfs(r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        if not grid:
            return 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1":
                    res += 1
                    self.dfs(r, c)
        return res