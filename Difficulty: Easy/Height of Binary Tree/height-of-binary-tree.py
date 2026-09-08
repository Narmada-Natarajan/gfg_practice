''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        
        if root==None:
            return -1
            
        lh=self.height(root.left)
        rh=self.height(root.right)
            
        return 1+max(lh,rh)
        