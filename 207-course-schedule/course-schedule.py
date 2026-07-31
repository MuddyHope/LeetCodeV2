class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        

        seen = set()

        def dfs(course):
            if not adj_list[course]:
                return True
            
            if course in seen:
                return False
            
            seen.add(course)

            for pre in adj_list[course]:
                if not dfs(pre) : return False
            
            adj_list[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True