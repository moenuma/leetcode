# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Use DFS
    # Space: O(n)
    def flatten1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root, queue):
            if not root: return
            queue.append(root)
            dfs(root.left, queue)
            dfs(root.right, queue)
        
        if not root: return root

        queue = deque()
        dfs(root, queue)
        cur = queue.popleft()
        
        while queue:
            cur.left = None
            nxt = queue.popleft()
            cur.right = nxt
            cur = nxt
    
    # Time: O(n)
    # Space: O(h) - h: height of tree
    def flatten2(self, root: Optional[TreeNode]) -> None:
        # flatten the root tree and return the list tail
        def dfs(root):
            if not root:
                return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            last = rightTail or leftTail or root
            return last
        
        dfs(root)
    