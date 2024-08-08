class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses={i:[] for i in range(numCourses)}
        for course in prerequisites:
            # if course[0]==course[1]:
            #     return False
            courses[course[0]].append(course[1])
        
        visited=[]
        seen=[False for _ in range(numCourses)]
        def dfs(current):
            if current in visited:
                return True
            if seen[current]:
                return False

            seen[current]=True

            for neighbor in courses[current]:
                if not dfs(neighbor):
                    return False
            visited.append(current)
            seen[current]=False
            return True
        
        for course in courses:
            if course not in visited:
                if not dfs(course):
                    return False

        return True