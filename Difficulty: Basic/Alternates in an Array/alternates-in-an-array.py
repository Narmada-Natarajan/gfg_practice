class Solution:
    def getAlternates(self, arr):
        
        n=len(arr)
        ans=[]
        
        for i in range(0,n,2):
            ans.append(arr[i])
        return ans
        