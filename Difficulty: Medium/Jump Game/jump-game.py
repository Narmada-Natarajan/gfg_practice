class Solution:
    def canReach(self, arr):
        
        n=len(arr)
        maxi=0
        
        for i in range(n):
            if i>maxi:
                return False
            else:
                maxi=max(maxi,i+arr[i])
        return True
        