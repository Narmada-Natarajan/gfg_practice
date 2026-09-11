class Solution:
    def dupLastIndex(self, arr):
        
        
        f={}
        ans=[-1,-1]
                
        for i in range(len(arr)):
            if arr[i] in f:
                ans=[i,arr[i]]
                
            f[arr[i]]=i
                
        return ans
    
