''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        
        if root==None:
            return []
            
        ans=[]
        
        def postorder(node):
            if node==None:
                return []
                
            postorder(node.left)
            postorder(node.right)
            ans.append(node.data)
            
        postorder(root)
        return ans
        
        