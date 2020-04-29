# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")
        self.findMax(root) 
        return self.res


    def findMax(self, root:TreeNode) -> int:
        if root is None:
            return 0
        l = self.findMax(root.left)
        r = self.findMax(root.right)
        maxlr = max(l,r)
        maxSingle = max(maxlr+root.val, root.val)

        maxAll = max(maxSingle, l+r+root.val)

        self.res = max(self.res, maxAll)

        return maxSingle