class Solution:
    def getMinMax(self, arr):
        # code here
        
        maxe=arr[0]
        mine=arr[0]
         
            
        for i in range(1,len(arr)):
            if arr[i]>maxe:
                maxe=arr[i]
            if arr[i]<mine:
                mine=arr[i]
        return [mine,maxe]
            
            