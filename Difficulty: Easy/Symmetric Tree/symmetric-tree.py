''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isSymmetric(self, root):
        
        if root is None:
            return True
            
        def mirror(a,b):
            
            if a is None and b is None:
                return True
                
            if a is None or b is None:
                return False
                
            if a.data !=b.data:
                return False
                
            return mirror(a.left,b.right) and mirror(a.right,b.left)
            
        return mirror(root.left,root.right)
            
        
        
        