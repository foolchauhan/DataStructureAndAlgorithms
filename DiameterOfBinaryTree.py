# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = [-999999999999]
        height_of_tree = self.height(root, ans)
        return ans[0]-1
    
    def height(self, root: TreeNode, ans:int) -> int:
        if (root is None): 
            return 0
        
        left_height = self.height(root.left, ans) 
        right_height = self.height(root.right, ans)  
        
        ans[0] = max(ans[0], 1 + left_height + right_height)  
        return 1 + max(left_height, right_height) 
