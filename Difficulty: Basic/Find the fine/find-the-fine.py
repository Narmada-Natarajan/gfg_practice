class Solution:
    def totalFine(self, date, car, fine):
        
        s=0
        evend=(date%2==0)
        
        for c,f in zip(car,fine):
            if (c%2!=0)==evend:
                s+=f
        return s
        
        
                    
            
        
        
    
    
    