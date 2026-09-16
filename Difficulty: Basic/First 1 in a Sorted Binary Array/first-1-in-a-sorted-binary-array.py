class Solution:
    def firstIndex(self, arr):
        
        
        for i in range(len(arr)):
            if arr[i]==1:
                return i
                break
        return -1
            

