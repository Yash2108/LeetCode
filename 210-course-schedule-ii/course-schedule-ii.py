class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        course_prereq = defaultdict(list)

        for course, prereq in prerequisites:
            course_prereq[course].append(prereq)

        visited=[]

        def dfs(course, seen):
            if course in visited:
                return True
            if course in seen:
                return False
            seen[course]=None

            for prereq in course_prereq[course]:
                if not dfs(prereq, seen):
                    return False
            del seen[course]
            visited.append(course)
            return True
        for course_num in range(numCourses):
            if not dfs(course_num, {}):
                return []
        return visited

