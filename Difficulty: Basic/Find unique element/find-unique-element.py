class Solution:
    def uniqueElement(self, arr: list[int], k: int) -> int:
        
        mp={}
        
        for i in arr:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        for i in mp:
            if mp[i]//k==0:
                return i
        

        