'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def isSumTree(self, node):
        
        def getSum(root):
            if root is None:
                return 0
                
            return root.data+ getSum(root.left)+ getSum(root.right)
        
        def check(root):
        
            if root is None:
                return True
            
            if root.left is None and root.right is None:
                return True
            
            l=getSum(root.left)
            r=getSum(root.right)
        
            if l+r !=root.data:
                return False
    
            return check(root.left) and check(root.right)
            
        return check(node)
            
        