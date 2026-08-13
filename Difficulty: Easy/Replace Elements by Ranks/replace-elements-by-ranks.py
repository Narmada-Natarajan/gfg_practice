class Solution:
    def replaceWithRank(self, arr):
        
        n=len(arr)
        temp=[]
        for i in range(n):
            temp.append((arr[i],i)) #values and original index 
            #[(10,0),(40,1),(20,2)]  
        
        temp.sort() #sort the arr #[(10,0),(20,2),(40,1)]  
        
        for r in range(n):  #r=0,1,2
            val,idx=temp[r]   #temp[0]=(10,0) , temp[1]=(20,2)
            arr[idx]=r #rank=0,rank=2,rank=1
        
        
        
        
        
            
            
            
                
                
        
        