class Solution:
    def countFreq(self, arr, target):
        
        f={}
        cnt=0
        for i in arr:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
                
        if target in f:
            return f[target]
        return 0        
            
        