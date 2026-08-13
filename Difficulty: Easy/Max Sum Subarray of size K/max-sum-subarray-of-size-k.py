class Solution:
    def maxSubarraySum(self, arr, k):
        
        n=len(arr)
        if n<k:
            return -1
        
        ws=sum(arr[:k]) #to store sum of windoe size k
        maxs=ws #current sum
        
        for i in range(k,n):
            ws+=arr[i]-arr[i-k] #old element enters and new element leaves
            maxs=max(ws,maxs)
            
        return max(maxs,ws)