class Solution:
    def minValueToBalance(self, arr: list[int]) -> int:
        
        mid=len(arr)//2
        
        left=arr[:mid]
        right=arr[mid:]
        
        lsum=sum(left)
        rsum=sum(right)
        
        if lsum>rsum:
            return lsum-rsum
        elif rsum>lsum:
            return rsum-lsum
        else:
            return 0
        
        