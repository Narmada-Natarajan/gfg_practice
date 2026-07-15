class Solution:
    def removeDuplicates(self, arr):
        # code here 
        
        ele=0
        res=[]
        
        for i in arr:
            if(i==ele):
                continue
            else:
                res.append(i)
                ele=i
        return res
            
                
            
        