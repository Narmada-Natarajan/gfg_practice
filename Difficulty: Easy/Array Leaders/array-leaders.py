class Solution:
    def leaders(self, arr):
        
        ans=[]
        maxi=float('-inf')
        
        for i in range(len(arr)-1,-1,-1): #Traverse from right to left
            if arr[i]>=maxi:
                ans.append(arr[i])
                maxi=arr[i]
                
        # Reverse for original order
        return ans[::-1]
        