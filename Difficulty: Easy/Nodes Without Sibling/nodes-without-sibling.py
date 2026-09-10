''' Definition of Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def noSibling(self, root):
        
        ans=[]
        
        if root is None:
            return [-1]
            
        def dfs(node):
            
            if node is None:
                return
                
                
            if node.left and not node.right:
                ans.append(node.left.data)
                
            if node.right and not node.left:
                ans.append(node.right.data)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
            
        if not ans:
            return[-1]
            
        ans.sort()    
        return ans
            
      

                

            
            
        
        
        
        
        
        
        