'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:
        1
       / \
      2   3
     /
    4       

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:
        1
       / \
      2   3
       \   \
        4   5

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:
        1
       / \
      2   3
       \   
        4   

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''

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
        