class Solution:
    def reverse(self, s: str) -> str:
        stack=[]
        
        for ch in s:
            stack.append(ch)
        
        ans=""   
        while stack:
            ans+=stack.pop()
            
        return ans