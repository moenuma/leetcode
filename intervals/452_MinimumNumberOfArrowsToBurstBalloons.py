class Solution:
    # Time: O(nlogn)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda i: i[0])

        minEnd = float("-inf")
        res = 0

        for start, end in points:
            if start <= minEnd:
                minEnd = min(minEnd, end)
            else:
                res += 1
                minEnd = end
        
        return res