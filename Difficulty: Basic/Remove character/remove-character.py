class Solution:
    def removeChars (ob, str1, str2):
        
        ans=""
        for i in str1:
            if i not in str2:
                ans+=i
        return ans
            
        