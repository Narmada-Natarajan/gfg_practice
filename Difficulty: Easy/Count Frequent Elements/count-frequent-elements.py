class Solution:
    def countOccurence(self,arr, k):
        
        f={}
        n=len(arr)
        
        for i in arr:
            if i in f:
                f[i]+=1
                
            else:
                f[i]=1
                
        cnt=0 
        for i in f:
            if f[i]>n/k:
                cnt+=1
        return cnt
        
        
        
        