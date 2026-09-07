class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        
        arr.sort()
        dep.sort()
        
        i=j=0
        p=0
        maxp=0
        
        while i<len(arr):
            if arr[i]<=dep[j]:
                p+=1
                maxp=max(maxp,p)
                i+=1
            
            else:
                p-=1
                j+=1
                
        return maxp
                
        