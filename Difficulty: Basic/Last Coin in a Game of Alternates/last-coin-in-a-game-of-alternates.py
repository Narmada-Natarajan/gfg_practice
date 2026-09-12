class Solution:
    def coin(self, arr):
        
        l=0
        r=len(arr)-1
        
        while l<r:
            if arr[l]>arr[r]:
                l+=1
                
            else:
                r-=1
                
        return arr[l]
        