# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Use str
    # Time: O(n)
    # Space: O(h)
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        def dfs(root, numStr):
            if not root:
                return 0
            
            numStr += str(root.val)

            # reached leaf node
            if not root.left and not root.right:
                return int(numStr)

            return dfs(root.left, numStr) + dfs(root.right, numStr)
        
        return dfs(root, "")
    
    # Use math
    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, num):
            if not cur:
                return 0
            
            num = num * 10 + cur.val

            if not cur.left and not cur.right:
                return num
            
            return dfs(cur.left, num) + dfs(cur.right, num)
        
        return dfs(root, 0)