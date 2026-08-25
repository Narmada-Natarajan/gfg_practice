class Solution:
    def  typeOfArr(self , arr):
        
        if arr==sorted(arr):
            return 1
        
        if arr==sorted(arr,reverse=True):
            return 2
        
        if arr[0]<arr[-1]:
            return 3
        
        return 4
        
        
    
    
