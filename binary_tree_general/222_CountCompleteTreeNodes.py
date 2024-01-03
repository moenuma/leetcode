# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    # DFS
    # Time: O(n)
    # Space: O(1)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return 1 + self.countNodes(root.left) + countNodes(root.right)

class Solution2:
    # Time: O(log^2(n))
    # Time: O(1)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        leftLevels = 1
        left = root.left

        while left:
            left = left.left
            leftLevels += 1
        
        rightLevels = 1
        right = root.right

        while right:
            right = right.right
            rightLevels += 1

        if leftLevels == rightLevels:
            return (2**leftLevels) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)