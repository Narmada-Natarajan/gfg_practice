class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        
        a=0
        b=1
        ans=[]
        
        for i in range(n):
            ans.append(a)
            c=a+b
            a=b
            b=c
        return ans
        