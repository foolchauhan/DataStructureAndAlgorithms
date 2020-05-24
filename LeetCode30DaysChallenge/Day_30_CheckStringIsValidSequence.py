# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            return len(arr) == 0
        return self.isValid(root, arr, 0)
    
    
    def isValid(self, root, arr, idx):
        if root.val != arr[idx]:
            return False
        if idx == len(arr)-1:
            return not root.right and not root.left
        return (root.left and self.isValid(root.left, arr, idx+1)) or (root.right and self.isValid(root.right, arr, idx+1))
        