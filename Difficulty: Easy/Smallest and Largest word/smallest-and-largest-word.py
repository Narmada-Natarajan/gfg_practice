class Solution:
    def smallerAndLarge(self, s: str) -> list[str]:
        
        words=s.split()
        small=words[0]
        large=words[0]
        
        for word in words:
            if len(word)<len(small):
                small=word
            if len(word)>=len(large):
                large=word
            
        
        return small,large

            
        