class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            mapping[course].append(prereq)
        
        def dfs(course, visited, seen):
            if course in visited:
                return True
            if course in seen:
                return False
            seen[course]=None
            for prereq in mapping[course]:
                if dfs(prereq, visited, seen):
                    visited.append(prereq)
                else:
                    return False
            del seen[course]
            visited.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course, [], {}):
                return False
        return True
