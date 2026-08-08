class Solution:
    def isPalindrome(self, s):
        # code here
        flag=False
        
        if s==s[::-1]:
            flag=True
                
        return flag
