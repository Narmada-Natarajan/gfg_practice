class Solution:
    def multiply(self, arr):
        
        mid=len(arr)//2
        
        left=arr[:mid]
        right=arr[mid:]
        
        lsum=sum(left)
        rsum=sum(right)
        
        return lsum*rsum