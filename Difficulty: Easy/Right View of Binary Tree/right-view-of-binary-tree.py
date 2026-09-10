'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self, root):
        
        if root is None:
            return 0
        
        q=deque()
        ans=[]
        
        q.append(root)
        
        while q:
            
            levelSize=len(q)
        
            for i in range(levelSize):
                
                root=q.popleft()
                
                if i==levelSize-1:
                    ans.append(root.data)
                    
                if root.left:
                    q.append(root.left)
                    
                if root.right:
                    q.append(root.right)
                    
        return ans
                    
    
        