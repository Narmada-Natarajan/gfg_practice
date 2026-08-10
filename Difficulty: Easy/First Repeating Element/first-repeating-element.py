class Solution:
    def firstRepeated(self, arr):
        
        f={}
        for i in arr:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        
        for i,e in enumerate(arr,start=1):
            if f[e]>1:
                return i
                
        return -1
        
        