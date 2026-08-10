class Solution:
	def pushZerosToEnd(self, arr):
    	
    	# if order doent matter-->two pointer
        # l=0
        # r=len(arr)-1
        
        # while l<r:
        #     if arr[l]!=0:
        #         l+=1
            
        #     elif arr[r]==0:
        #         r-=1
                
        #     else:
        #         arr[l],arr[r]=arr[r],arr[l]
        #         l+=1
        #         r-=1
                
        # return arr
        
        #if order matters
        
        l=0
        for r in range(len(arr)):
            if arr[r]!=0:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
        return arr
            
        
        
            
        
    	        
    	        
    	