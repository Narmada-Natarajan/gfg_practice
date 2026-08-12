class Solution:
    def maxConsecBits(self, arr):
        
        maxcnt=0
        cnt=1
        
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                cnt+=1
            else:
                maxcnt=max(maxcnt,cnt)
                cnt=1
                
        return max(maxcnt,cnt)
        
        