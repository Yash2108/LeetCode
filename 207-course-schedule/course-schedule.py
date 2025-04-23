class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            mapping[course].append(prereq)
        
        def dfs(course, visited, seen):
            seen[course]=None
            for prereq in mapping[course]:
                # seen[prereq]=None
                if prereq in visited:
                    continue
                if prereq in seen:
                    return False
                if dfs(prereq, visited, seen):
                    visited.append(prereq)
                    # del seen[prereq]
                else:
                    return False
            del seen[course]
            visited.append(course)
            return True
                    

        for course in range(numCourses):
            if not dfs(course, [], {}):
                return False
        return True
        '''

        take course and prereq
        add course to seen
        if all prereq in visited, add course to visited and remove from seen
        if prereq in seen, return False
        after all courses have been iterated return True

        '''