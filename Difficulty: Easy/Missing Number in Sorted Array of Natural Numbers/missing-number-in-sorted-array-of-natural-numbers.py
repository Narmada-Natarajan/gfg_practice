class Solution:
    def missingNumber(self, arr):
        
        n=len(arr)+1
        
        total=sum(arr)
        
        expected=n*(n+1)//2
        
        missing=expected-total
        
        return missing
        
        
        
        
        
        
    
        