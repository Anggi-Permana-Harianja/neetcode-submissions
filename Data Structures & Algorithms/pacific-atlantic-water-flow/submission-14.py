class Solution:
    def dfs(self, r, c, visited, prev_height):
        if (
            (r, c) in visited
            or r < 0 or c < 0 
            or r >= self.rows or c >= self.cols
            or self.heights[r][c] < prev_height
        ):
            return
        visited.add((r, c))
        curr_height = self.heights[r][c]
        self.dfs(r - 1, c, visited, curr_height)
        self.dfs(r + 1, c, visited, curr_height)
        self.dfs(r, c + 1, visited, curr_height)
        self.dfs(r, c - 1, visited, curr_height)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        self.heights = heights
        self.rows, self.cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for col in range(self.cols):
            # pacific
            self.dfs(0, col, pacific, self.heights[0][col])
            # atlantic
            self.dfs(self.rows - 1, col, atlantic, self.heights[self.rows - 1][col])
        for row in range(self.rows):
            # pacific
            self.dfs(row, 0, pacific, self.heights[row][0])
            # atlantic
            self.dfs(row, self.cols - 1, atlantic, self.heights[row][self.cols - 1])
        return [[row, col] for row in range(self.rows) for col in range(self.cols) if (row, col) in pacific and (row, col) in atlantic]