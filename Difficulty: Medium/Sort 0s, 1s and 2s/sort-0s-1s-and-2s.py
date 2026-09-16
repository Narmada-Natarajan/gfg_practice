class Solution:
    def sort012(self, arr):
        
        s=0
        m=0
        e=len(arr)-1
        
        while m<=e:
            
            element=arr[m]
            
            if element==0:
                arr[m],arr[s]=arr[s],arr[m]
                s+=1
                m+=1
                
            elif element==1:
                m+=1
                
            else: 
                arr[m],arr[e]=arr[e],arr[m]
                e-=1
                
            
                
        