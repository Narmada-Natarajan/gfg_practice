class Solution:
    def findTwoElement(self, arr):
        
        n=len(arr)
        freq=[0]*(n+1) #create freq array
        dup=miss=-1
        
        for x in arr:
            freq[x]+=1
            
        #finding dup and missing
        
        for i in range(1,n+1):
            if freq[i]==2:
                dup=i
            elif freq[i]==0:
                miss=i
        return [dup,miss]
            
        
        

