class Solution:
    def pattern(self, n):
        
        ans=[]
        
        def pat(x:int):
    
            ans.append(x)
            
            if x<=0:
                return
            
            pat(x-5)
            
            ans.append(x)
            
        pat(n)
        return ans
            
            
            
        
            
        
        
        