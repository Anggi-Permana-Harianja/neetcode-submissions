class Solution:
    def dfs(self, r, c, visit, prev_heights):
        if (
            (r, c) in visit
            or r < 0 
            or c < 0
            or r == self.rows
            or c == self.cols
            or self.heights[r][c] < prev_heights
        ):
            return
        visit.add((r, c))
        height = self.heights[r][c]
        self.dfs(r - 1, c, visit, height)
        self.dfs(r + 1, c, visit, height)
        self.dfs(r, c - 1, visit, height)
        self.dfs(r, c + 1, visit, height)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.rows = len(heights)
        self.cols = len(heights[0])
        pac = set()
        atl = set()
        for c in range(self.cols):
            # pacific
            self.dfs(0, c, pac, heights[0][c])
            # atlantic
            self.dfs(self.rows - 1, c, atl, heights[self.rows - 1][c])
        for r in range(self.rows):
            # pacific
            self.dfs(r, 0, pac, heights[r][0])
            # atlantic
            self.dfs(r, self.cols - 1, atl, heights[r][self.cols - 1])
        return [[r, c] for r in range(self.rows) for c in range(self.cols) if (r, c) in pac and (r, c) in atl]