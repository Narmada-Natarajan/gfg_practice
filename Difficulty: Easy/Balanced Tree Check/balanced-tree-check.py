''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
       
       def height(node):
           
           if node is None:
               
               return 0
               
           l=height(node.left)
           r=height(node.right)
            
           if l==-1 or r==-1:
               
               return -1
               
           if abs(l-r)>1:
               return -1
                
           return 1+max(l,r)
           
       return height(root)!=-1
            
            
            