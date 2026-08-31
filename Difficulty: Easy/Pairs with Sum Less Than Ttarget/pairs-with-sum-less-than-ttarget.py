class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        
        arr.sort()
        
        l=0
        r=len(arr)-1
        t=0
        cnt=0
        
        for i in arr:
            t=arr[l]+arr[r]
            
            if t<target:
                cnt+=(r-l)
                l+=1
            else:
                r-=1
        
        return cnt
                
        