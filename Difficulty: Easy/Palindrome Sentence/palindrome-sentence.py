class Solution:
	def isPalinSent(self, s):
		
		sen=[ch.lower() for ch in s if ch.isalnum()]
		
		return sen==sen[::-1]
		