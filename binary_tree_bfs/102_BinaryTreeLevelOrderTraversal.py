# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)
    # Space: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = deque([root])

        while queue:
            levelRes = []
            queueLen = len(queue)

            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    levelRes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            if levelRes:
                res.append(levelRes)

        return res