'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        
        if root is None:
            return []
            
        q=deque([(root,0)])
        mp={}
        
        while q:
            
            root,hd=q.popleft()
            
            mp[hd]=root.data
        
            if root.left:
                q.append((root.left,hd-1))
                
            if root.right:
                q.append((root.right,hd+1))
                
        return [mp[x]for x in sorted(mp)]
                
        