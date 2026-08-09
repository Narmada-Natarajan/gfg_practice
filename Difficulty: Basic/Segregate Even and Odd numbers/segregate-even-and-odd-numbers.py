class Solution:

	def segregateEvenOdd(self,arr):
		
		even=[]
		
		for i in arr:
		    if i%2==0:
		        even.append(i)
		
		odd=[]
		for i in arr: 
		    if i%2!=0:
		        odd.append(i)
		
		even.sort()   
		odd.sort()
		arr[:]=even+odd
		
		
		