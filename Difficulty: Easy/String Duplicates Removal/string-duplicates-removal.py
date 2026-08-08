class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    
	    seen=""
	    ans=""
	    for ch in s:
	        if ch not in seen:
	            ans+=ch
	            seen+=ans
	    return ans
	            
	            
	    