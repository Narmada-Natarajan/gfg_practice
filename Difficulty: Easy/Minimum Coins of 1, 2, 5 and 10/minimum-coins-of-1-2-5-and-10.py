class Solution:
    def findMin(self, n: int) -> int:
        
        cnt=0
        
        for coins in [10,5,2,1]:
            
            while n>=coins:
                n-=coins
                cnt+=1
        return cnt
            
        
    
       
       