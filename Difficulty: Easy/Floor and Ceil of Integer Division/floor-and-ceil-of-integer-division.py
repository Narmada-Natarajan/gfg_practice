import math

class Solution:
    def divFloorCeil(self, a, b):
        ans=[]
        f=math.floor(a/b)
        c=math.ceil(a/b)
        ans.append(f)
        ans.append(c)
        return ans
