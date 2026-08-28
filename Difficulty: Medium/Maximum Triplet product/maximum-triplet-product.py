class Solution:
    def maxTripletProduct(self, arr: list[int]) -> int:
        
        n=len(arr)
        
        arr.sort()
        
        return max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])
        