class Solution:
    def getMaxOccuringChar(self, s):
        # code here
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxf=0
        ans=""
        for i  in freq:
            if(freq[i]>maxf):
                maxf=freq[i]
                ans=i
            elif freq[i] == maxf and i < ans:
                ans = i
        return ans
            