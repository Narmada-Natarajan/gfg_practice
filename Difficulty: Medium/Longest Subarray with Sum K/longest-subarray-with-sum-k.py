class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        prefix={}
        cur_sum=0
        ans=0 #max length
        
        
        for i in range(len(arr)):
            cur_sum+=arr[i] #add current element to running sum
                
            if cur_sum==k:
                ans=i+1
                
            if(cur_sum-k) in prefix:
                ans=max(ans,i-prefix[cur_sum-k])
                
            if cur_sum not in prefix:
                prefix[cur_sum]=i
                
                
        return ans
    
