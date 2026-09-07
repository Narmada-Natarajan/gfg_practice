class Solution:
    def minJumps(self, arr: list[int]) -> int:
        
        jumps=0
        cur_end=0
        farthest=0
        
        for i in range(len(arr)-1):
            farthest=max(farthest,i+arr[i])
            
            if i==cur_end:
            
                if farthest==cur_end:
                    return -1
                
                jumps+=1
                cur_end=farthest
                
        return jumps
                

            
        
            
        
                
                
        
        
        