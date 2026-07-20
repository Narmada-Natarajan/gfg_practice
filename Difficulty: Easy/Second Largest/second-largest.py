import heapq

class Solution:
    def getSecondLargest(self, arr):
        # code here
        
        arr=list(set(arr))
        
        if len(arr)<2:
            return -1
            
        return heapq.nlargest(2,arr)[1]
        
        
        
        
        
        