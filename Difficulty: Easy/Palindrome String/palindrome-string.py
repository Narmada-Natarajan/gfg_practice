class Solution:
    def isPalindrome(self, s):
        
        flag=False
        
        if s==s[::-1]:
            flag=True
                
        return flag
