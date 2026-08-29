import math

class Solution:
    def commDiv(self, a, b):
        
        g=math.gcd(a,b)
    
        cnt=0
        
        for i in range(1,math.isqrt(g)+1):
            if g%i==0:
                cnt+=1
                
                if i*i!=g:
                    cnt+=1
                
        return cnt
        
        
            
        