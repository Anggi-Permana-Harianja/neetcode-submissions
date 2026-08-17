class Solution:
    def dfs(self, course):
        if course in self.visited:
            return False
        if self.precoursemap[course] == []:
            return True
        self.visited.add(course)
        for precourse in self.precoursemap[course]:
            if not self.dfs(precourse):
                return False
        self.visited.remove(course)
        self.precoursemap[course] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.precoursemap = {i: [] for i in range(numCourses)}
        for course, precourse in prerequisites:
            self.precoursemap[course].append(precourse)
        self.visited = set()
        for course in range(numCourses):
            if not self.dfs(course):
                return False
        return True