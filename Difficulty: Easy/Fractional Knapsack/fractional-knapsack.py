class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        
        items=list(zip(val,wt))
        
        items.sort(key=lambda x:x[0]/x[1],reverse=True)
        
        total=0
        
        for value,weight in items:
            if capacity>=weight:
                total+=value
                capacity-=weight
                
            else:
                ratio=value/weight
                total+=ratio*capacity
                break
            
        return total
                
                
                
            
        
        
      
            
        
        
        
        
        
        
        
        
        
        
        