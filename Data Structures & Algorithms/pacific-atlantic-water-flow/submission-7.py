class Solution:
    def dfs(self, r, c, visited, prev_heights):
        if (
            r < 0 or c < 0 
            or r == self.rows or c == self.cols
            or self.heights[r][c] < prev_heights
            or (r, c) in visited
        ):
            return
        visited.add((r, c))
        height = self.heights[r][c]
        self.dfs(r - 1, c, visited, height)
        self.dfs(r + 1, c, visited, height)
        self.dfs(r, c - 1, visited, height)
        self.dfs(r, c + 1, visited, height)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.rows, self.cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for col in range(self.cols):
            # pacific
            self.dfs(0, col, pacific, heights[0][col])
            # atlantic
            self.dfs(self.rows - 1, col, atlantic, self.heights[self.rows - 1][col])
        for row in range(self.rows):
            # pacific
            self.dfs(row, 0, pacific, self.heights[row][0])
            # atlantic
            self.dfs(row, self.cols - 1, atlantic, self.heights[row][self.cols - 1])
        return [[row, col] for row in range(self.rows) for col in range(self.cols) if (row, col) in pacific and (row, col) in atlantic]