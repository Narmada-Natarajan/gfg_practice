class Solution:
    def search(self, pat, txt):
        
        ans=[]
    
        m, n = len(pat),len(txt)
        
        for i in range(n - m + 1):
            
            if txt[i : i + m] == pat:
                ans.append(i) 

        return ans

            
        