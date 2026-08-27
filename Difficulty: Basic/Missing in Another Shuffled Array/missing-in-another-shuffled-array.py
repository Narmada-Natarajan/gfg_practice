class Solution:
    def findMissing(self, arr1,arr2):
        
        arr1.sort()
        arr2.sort()
        for i in range(len(arr2)):
            if arr1[i] != arr2[i]:
                return arr1[i]
        return arr1[-1]
                
        
