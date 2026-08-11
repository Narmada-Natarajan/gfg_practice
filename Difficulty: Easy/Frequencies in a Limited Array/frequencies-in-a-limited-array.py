class Solution:
    def frequencyCount(self, arr):
        
        f={}
        for i in arr:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
                
        ans=[]   
        
        for i in range(1,len(arr)+1):
            # ans.append(f.get(i,0))
            if i in f:
                ans.append(f[i])
            else:
                ans.append(0)
        return ans
                
                
            
        
                
                
            
            
        

