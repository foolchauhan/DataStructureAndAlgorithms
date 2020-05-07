from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:  
   
        if root == None: 
            return False 
    
        parA = None 
    
        parB = None 
    
        q = []  
    
        tmp = TreeNode(-1)  
    
        q.append((root, tmp))  
        
        while len(q) > 0:   
            levSize = len(q)  
            while levSize:   
    
                ele = q.pop(0)  
    
                if ele[0].val == x:   
                    parA = ele[1]  
                
                if ele[0].data == y:   
                    parB = ele[1]  
    
                if ele[0].left:   
                    q.append((ele[0].left, ele[0]))  
                
                if ele[0].right:   
                    q.append((ele[0].right, ele[0]))  
                levSize -= 1
    
                if parA and parB:  
                    break 
    
            if parA and parB:   
                return parA != parB  
    
            if (parA and not parB) or (parB and not parA):  
                return False         
        return False 
        