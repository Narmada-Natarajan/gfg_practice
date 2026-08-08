class Solution:
	def countOddEven(self, arr):
		
		cnt_even=0
		cnt_odd=0
		
		for i in arr:
		    if i%2==0:
		        cnt_even+=1
		    else:
		        cnt_odd+=1
		        
		return cnt_odd,cnt_even
		
		