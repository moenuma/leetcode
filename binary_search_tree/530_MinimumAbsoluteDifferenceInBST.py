# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    minDiff = float("inf")
    prev = None
    # Time: O(n)
    # Space: O(1)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # inorder traversal
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            
            if self.prev != None:
                self.minDiff = min(self.minDiff, abs(self.prev - node.val))
            self.prev = node.val
            
            dfs(node.right)
        
        dfs(root)
        return self.minDiff