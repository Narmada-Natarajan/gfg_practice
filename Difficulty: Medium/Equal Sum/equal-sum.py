class Solution:
	def equilibrium(self,arr): 
    	
    	total=sum(arr)
    	leftsum=0
    	
    	for x in arr:
    	    if leftsum==(total-leftsum-x):
    	        return "true"
    	    leftsum+=x
    	return "false"
    
    	
    	
    	
    
    	        
    	