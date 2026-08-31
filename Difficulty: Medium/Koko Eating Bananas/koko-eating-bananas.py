import math

class Solution:
    def kokoEat(self, arr, k):
    
        low=1
        
        high=max(arr)
        
        while low<high:
            mid=(low+high)//2
            
            hours=0
            
            for b in arr:
                hours+=math.ceil(b/mid)
                
            if hours<=k:
                high=mid
                
            else:
                low=mid+1
        
        return low
        
        