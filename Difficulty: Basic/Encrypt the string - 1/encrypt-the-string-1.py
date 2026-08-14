class Solution:

    def encryptString(self, s):
        
        ans=""
        i=len(s)-1
        while i>=0:
            ch=s[i]
            count=0
            
            while i>=0 and ch==s[i]:
                count+=1
                i-=1
            
            ans+=str(count)[::-1]+ch
        return ans
        
        
            
        
       
        
        
            