class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb):
            if len(comb) == k:
                res.append(comb)
                return
            if i > n:
                return
            backtrack(i+1, comb + [i]) # include
            backtrack(i+1, comb) # not include

        backtrack(1, [])
        return res
    
    # Time: O(k*n^k)
    def combine2(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb)
                return

            for i in range(j, n + 1):
                backtrack(i+1, comb+[i])
        
        backtrack(1, [])
        return res