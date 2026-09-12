class Solution:

    def isGoodOrBad(self, s: str) -> bool:
        
        vowels=set('aeiou')
        vcnt=0
        ccnt=0
        
        for char in s:
            if char in vowels:
                vcnt+=1
                ccnt=0
                
            elif char=="?":
                vcnt+=1
                ccnt+=1
            
            else:
                ccnt+=1
                vcnt=0
                
        
            if vcnt>5 or ccnt>3:
                return 0
        return 1
        
        
            
            
                
                
            
