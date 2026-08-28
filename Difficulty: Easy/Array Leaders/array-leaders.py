class Solution:
    def leaders(self, arr):
        
        maxr=arr[-1]
        ans=[arr[-1]]
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>=maxr:
                maxr=arr[i]
                ans.append(maxr)
                
        return ans[::-1]