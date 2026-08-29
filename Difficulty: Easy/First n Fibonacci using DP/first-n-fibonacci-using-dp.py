class Solution:
    def fibonacciNumbers(self, n):
        
        a=0
        b=1
        ans=[]
        mod=10**9+7
        
        for i in range(n+1):
            ans.append(a)
            c=(a+b)%mod
            a=b
            b=c
        return ans
            
            
            