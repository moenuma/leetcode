class Solution:
    # Time: O(2^T)
    # T - target
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            # base case 1
            if total == target:
                res.append(cur[:])
                return
            # base case 2
            if i >= len(candidates) or total > target:
                return
            
            # decision 1: include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])

            # decision 2: don't include candidates[i]
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)

        return res