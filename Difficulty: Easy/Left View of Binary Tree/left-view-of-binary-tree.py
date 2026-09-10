''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self, root):
        
        if root is None:
            return []
        
        q=deque()
        ans=[]
        
        q.append(root)
        
        while q:
            
            levelSize=len(q)
            
            for i in range(levelSize):
                node=q.popleft()
                
                if i==0:
                    ans.append(node.data)
                    
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return ans
                
        
        