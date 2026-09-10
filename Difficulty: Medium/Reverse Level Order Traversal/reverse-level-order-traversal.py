''' Structure of Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def reverseLevelOrder(self, root):
        
        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level.reverse()
            ans.extend(level)

        return ans[::-1]