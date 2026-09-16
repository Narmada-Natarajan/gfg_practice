class Solution:
    def findDiff(self, arr):
        
        if not arr:
            return 0
        
        f={}
        
        for i in arr:
            if i in f:
                f[i]+=1
                
            else:
                f[i]=1
                
        return max(f.values())-min(f.values())
            
            
             
            
                
    
    
    
    