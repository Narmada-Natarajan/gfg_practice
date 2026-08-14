class Solution:
    def removeChars(self, s: str) -> str:
        
        ans=""
        for i in s:
            if i.isalpha():
                ans+=i
        return ans
        