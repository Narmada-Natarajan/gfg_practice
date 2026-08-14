class Solution:
	def removeVowels(self, s):
		ans=""
		for i in s:
		    if i not in "aeiou":
		        ans+=i
		return ans
		