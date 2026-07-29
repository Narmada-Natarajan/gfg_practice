class Solution:
    def findDuplicates(self, arr):
        # code here
        map={}
        ans=[]
        
        for i in arr:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        
        for i in map:
            if map[i]==2:
                ans.append(i)
        return ans
                
                
                
        
       