class Solution:
    def findSum(self, arr):
        
        
        a=set(arr)
        
        if len(a)==1:
            return next(iter(a))
        
        else:
            return sum(a)
        
        
       