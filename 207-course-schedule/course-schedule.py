class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj_list = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        seen = set()
        
        def dfs(course):
            if course in seen:
                return False
            
            if adj_list[course] == []:
                return True
            
            seen.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq): return False
            seen.remove(course)
            adj_list[course] = []
            return True
    
        for i in range(numCourses):
            if not dfs(i): return False
        return True
