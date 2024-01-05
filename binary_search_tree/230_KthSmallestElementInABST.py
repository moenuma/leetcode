# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
# Time: O(n)
# Space: O(1)
class Solution1:
    cnt = 0
    res = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
            dfs(node.right)
        
        dfs(root)
        return self.res

# Iterative
# Time: O(n)
# Space: O(n)
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # num of visited nodes
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right

