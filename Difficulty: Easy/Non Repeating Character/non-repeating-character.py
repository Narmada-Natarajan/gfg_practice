class Solution:
    def nonRepeatingChar(self,s):
        f={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for i in f:
            if f[i]==1:
                return i
        return "$"
    
    