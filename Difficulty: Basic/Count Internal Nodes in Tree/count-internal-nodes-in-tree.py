# Binary Tree Node Structure
'''class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def countNonLeafNodes(self, root):
        
        if root==None:
            return 0
            
        if root.left is None and root.right is None:
            return 0
            
        return 1+self.countNonLeafNodes(root.left)+self.countNonLeafNodes(root.right)