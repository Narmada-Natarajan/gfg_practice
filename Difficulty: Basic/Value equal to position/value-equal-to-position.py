class Solution:
    def valEqualToPos(self, arr):
        
        n=len(arr)
        ans=[]
        
        for i,e in enumerate(arr,start=1):
            if e==i:
                ans.append(i)
        return ans
                
                