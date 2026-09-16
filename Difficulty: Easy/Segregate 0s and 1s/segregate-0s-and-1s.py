class Solution:
    def segregate0and1(self, arr):
        
        l=0
        r=len(arr)-1
        
        while l<=r:
            
            if arr[l]==1:
                arr[l],arr[r]=arr[r],arr[l] #swap
                r-=1
                
            else:
                l+=1
                
        
                
                