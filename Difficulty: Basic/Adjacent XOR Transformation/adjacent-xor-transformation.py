class Solution:
    def xorArray(self, arr):
        
        for i in range(len(arr)-1):
        
            arr[i]=arr[i]^arr[i+1]
            
        return arr
        