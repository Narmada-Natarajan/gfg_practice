
class Solution:
    def swapKth(self, arr, k):
     
        if 1 <= k <= len(arr):   
            left=k-1
            right=len(arr)-k
            arr[left],arr[right]=arr[right],arr[left]
        return arr
        
