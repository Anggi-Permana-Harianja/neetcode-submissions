class Solution:
    def dfs(self, r, c):
        if(
            r < 0 or c < 0 
            or r >= self.rows or c >= self.cols
            or self.grid[r][c] == 0
            or (r, c) in self.visited
        ):
            return 0
        self.visited.add((r, c))
        return 1 + self.dfs(r + 1, c) + self.dfs(r - 1, c) + self.dfs(r, c + 1) + self.dfs(r, c - 1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                res = max(res, self.dfs(r, c))
        return res