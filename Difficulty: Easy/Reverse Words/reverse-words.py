class Solution:
    def reverseWords(self, s):
        
        words = [x for x in s.split(".") if x]
        return ".".join(words[::-1])
        