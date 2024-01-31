class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openNum, closeNum):
            if openNum == closeNum == n:
                res.append("".join(stack))
                return
            
            if openNum < n:
                stack.append("(")
                backtrack(openNum+1, closeNum)
                stack.pop()
            
            if closeNum < openNum:
                stack.append(")")
                backtrack(openNum, closeNum+1)
                stack.pop()
            
        backtrack(0, 0)
        return res