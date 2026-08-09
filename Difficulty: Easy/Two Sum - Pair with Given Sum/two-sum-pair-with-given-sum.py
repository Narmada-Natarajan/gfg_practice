class Solution:
	def twoSum(self, arr, target):
	    
	    arr.sort()
		
		n=len(arr)
		left=0
		right=n-1
		
		
		while left<right:
		    total=arr[left]+arr[right]
		    
		    if total>target:
		        right-=1
		    
		    elif total<target:
		        left+=1
		    
		    else:
		        return True
		  
	    return False
		
		
		
		