# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)
    # Space: O(1)
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = []
        queue.append((root, 0))
        levels = {}

        while queue:
            
            node, level = queue.pop()
            
            if node:
                levels[level] = node.val
                if node.right:
                    queue.append((node.right, level+1))
                if node.left:
                    queue.append((node.left, level+1))

        return [val for val in levels.values()]
    
    # Time: O(n)
    # Space: O(1)
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            rightSide = None
            queueLen = len(queue)

            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                res.append(rightSide.val)
        
        return res