# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)
    # Space: O(n)
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root] if root else [])

        while queue:
            
            level = []
            queueLen = len(queue)

            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            level = reversed(level) if len(res) % 2 else level
            res.append(level)

        return res