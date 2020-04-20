# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(preorder, 0, len(preorder)-1)
    
    def buildTree(self, preorder: List[int], l:int, r:int) -> TreeNode:
        if l>r:
            return None
        root = TreeNode(preorder[l])
        if l==r:
            return root
        idx = l+1
        while idx<=r and preorder[idx] < preorder[l]:
            idx+=1
        root.left = self.buildTree(preorder, l+1, idx-1)
        root.right = self.buildTree(preorder, idx, r)

        return root


