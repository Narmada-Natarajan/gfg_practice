class Solution:
    def getOddOccurrence(self, arr):
        
        ans=0
        
        for x in arr:
            ans^=x
        return ans
        
            
        