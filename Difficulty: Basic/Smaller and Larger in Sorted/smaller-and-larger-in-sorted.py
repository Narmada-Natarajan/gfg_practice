class Solution:
    def getMoreAndLess(self, arr, target):
        
        less=0
        more=0
        for i in arr:
        
            if i<=target:
                less+=1
            if i>=target:
                more+=1
        return[less,more]
            
        