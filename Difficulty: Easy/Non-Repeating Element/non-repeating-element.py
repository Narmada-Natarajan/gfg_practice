class Solution:
    def firstNonRepeating(self, arr): 
        # code here
    
        hashmap={}
        n=len(arr)
    
        for i in arr:
            if(i in hashmap):
                hashmap[i]=hashmap[i]+1
            else:
                hashmap[i]=1
    
        for i in hashmap:
            val=hashmap[i]
            if val==1:
                return i
        return 0