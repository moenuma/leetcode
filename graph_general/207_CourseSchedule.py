class Solution:
    # Time: O(n+p)
    # n - numCourses
    # p - number of prerequisites
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqDict = collections.defaultdict(list)

        for pre, crs in prerequisites:
            prereqDict[pre].append(crs)

        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if prereqDict[crs] == []:
                return True
            visit.add(crs)
            for pre in prereqDict[crs]:
                if not dfs(pre): return False
            
            visit.remove(crs)
            prereqDict[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True