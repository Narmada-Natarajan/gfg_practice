class Solution:
    def maxChildren(self, greed, cookie):
        
        n=len(greed)
        m=len(cookie)
        
        greed.sort()
        cookie.sort()
        
        left=0
        right=0
        count=0
        
        while left<n and right<m:
            if greed[left]<=cookie[right]:
                count+=1
                left+=1
            right+=1
            
        return count
                
            
        
        

        
        
