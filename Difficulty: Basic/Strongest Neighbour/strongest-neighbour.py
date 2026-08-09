class Solution:
    def maxAdj(self, arr):
        
        # if len(arr)<2:
        #     return []
            
        ans=[]
    
        for i in range(0,len(arr)-1):
            ans.append(max(arr[i],arr[i+1]))
        return ans

                
        
        
        
        
        