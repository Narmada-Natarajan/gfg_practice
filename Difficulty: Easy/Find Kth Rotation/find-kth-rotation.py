class Solution:
    def findKRotation(self, arr):
        
        n=len(arr)
        mine=arr[0]
        mini=0
        
        for i in range(0,n):
            if mine>arr[i]:
                mini=i
                return mini
        return 0
        