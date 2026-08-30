class Solution:
    def maxConsecutiveOnes(self, n):
        
        cnt=0
        maxc=0
        
        b=list(bin(n)[2:])
        
        for i in b:
            if i=="1":
                cnt+=1
            else:
                cnt=0
                
            maxc=max(maxc,cnt)
            
        return maxc


