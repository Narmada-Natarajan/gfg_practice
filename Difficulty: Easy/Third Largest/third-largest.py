import heapq
class Solution:
    def thirdLargest(self,arr):
        
        if len(arr)>=3:    
        
            return heapq.nlargest(3,arr)[2]
    
        return -1
    
    
        
        
    
        