''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def levelOrder(self, root):
        
        ans=[]
        q=deque()
        
        if root is None:
            return ans
            
        q.append(root)
        
        while q:
            
            e=q.popleft() 
            ans.append(e.data)
            
            if e.left is not None:
                q.append(e.left)
                
            if e.right is not None:
                q.append(e.right)
                
        return ans
                
        
            
        