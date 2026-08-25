class Solution:
    def fibonacciNumbers(self,n):
        
        a=0
        b=1
        ans=[]
        
        for i in range(n):
            ans.append(a)
            c=a+b
            a=b
            b=c
        return ans
        