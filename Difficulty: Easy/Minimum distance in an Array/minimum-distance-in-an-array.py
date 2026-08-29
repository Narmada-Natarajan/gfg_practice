
class Solution:
    def minDist(self, arr, x, y):
        
        
        lx=-1
        ly=-1
        ans=float('inf')
        
        for i in range(len(arr)):
            if arr[i]==x:
                lx=i
                
            if arr[i]==y:
                ly=i
                
            if lx!=-1 and ly!=-1:
                ans=min(ans,abs(lx-ly))
                
        if ans==float('inf'):
            return -1
                
        return ans
                
        