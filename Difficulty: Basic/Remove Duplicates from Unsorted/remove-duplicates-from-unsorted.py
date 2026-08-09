class Solution:
    def removeDuplicate(self, arr):
        
        seen=set()
        ans=[]
        for i in arr:
            if i not in seen:
                ans.append(i)
                seen.add(i)
        return ans
        
        
    

