class Solution:
    def sumExceptFirstLast(self,arr):
        
        if len(arr)==2:
            return 0
            
        return sum(arr)-arr[0]-arr[-1]