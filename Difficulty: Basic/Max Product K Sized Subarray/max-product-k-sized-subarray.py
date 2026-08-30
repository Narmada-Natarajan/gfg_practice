class Solution:
    def findMaxProduct(self, arr, k):
        
        pro=1
        for i in range(k):
            pro*=arr[i]
        ans=pro
            
        for i in range(k,len(arr)):
            pro//=arr[i-k]
            pro*=arr[i]
            ans=max(ans,pro)
            
        return ans
            
        
        
        
        