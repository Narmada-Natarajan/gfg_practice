class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        l=0
        cur_sum=0
        
        for r in range(len(arr)):
            cur_sum+=arr[r]
            
            while cur_sum>target and l<=r:
                cur_sum-=arr[l]
                l+=1
            if cur_sum==target:
                return [l+1,r+1]
        
        return [-1]