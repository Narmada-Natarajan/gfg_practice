'''Structure of Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        if root==None:
            return []
            
        ans=[]
        
        def preorder(node):
            
            if node==None:
                return []
                
            ans.append(node.data)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ans
    