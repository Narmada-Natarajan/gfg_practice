''' Structure of binary tree node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        
        self.ans=float("-inf")
        
        def solve(node):
            if node==None:
                return 0
                
            left=max(0,solve(node.left))
            right=max(0,solve(node.right))
            
            self.ans=max(self.ans,node.data+left+right)
            
            return node.data+max(left,right)
            
        solve(root)
        return self.ans
        