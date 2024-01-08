class Solution:
    # Time: O(V + E)
    # V - number of prerequisites
    # E - number of courses (numCourses)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = collections.defaultdict(list)

        for pre, crs in prerequisites:
            prereqMap[pre].append(crs)

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereqMap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return output