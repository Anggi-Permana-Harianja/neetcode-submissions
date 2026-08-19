class Solution:
    def dfs(self, r, c):
        if (
            r < 0 or c < 0 
            or r >= self.rows or c >= self.cols
            or (r, c) in self.visited
            or self.grid[r][c] == 0
        ):
            return 0
        self.visited.add((r, c))
        return 1 + self.dfs(r - 1, c) + self.dfs(r + 1, c) + self.dfs(r, c - 1) + self.dfs(r, c + 1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()
        res = 0
        for r in range(self.rows):
            for c in range(self.cols):
                res = max(res, self.dfs(r, c))
        return res
        