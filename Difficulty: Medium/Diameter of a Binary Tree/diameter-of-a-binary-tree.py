''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        
        self.ans = 0

        def height(node):
            if node is None:
                return 0

            lh = height(node.left)
            rh = height(node.right)

                    # Diameter in edges
            self.ans = max(self.ans, lh + rh)

            return 1 + max(lh, rh)

        height(root)
        return self.ans