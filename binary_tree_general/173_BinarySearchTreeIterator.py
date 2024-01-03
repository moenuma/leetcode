# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator1:
    # DFS - recursive
    # Time: O(n)
    # Space: O(n)
    def __init__(self, root: Optional[TreeNode]):
        def dfs(root, lst):
            if not root: return

            dfs(root.left, lst)
            lst.append(root)
            dfs(root.right, lst)

        self.traversal = [float("-inf")]
        dfs(root, self.traversal)
        self.ptr = 0

    # Time: O(1)
    def next(self) -> int:
        self.ptr += 1
        return self.traversal[self.ptr].val

    # Time: O(1)
    def hasNext(self) -> bool:
        return len(self.traversal) - 1 > self.ptr

class BSTIterator2:
    # DFS - iterative
    # Time: O(n)
    # Space: O(h)
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # Average Time: O(1)
    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    # Time: O(1)
    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()