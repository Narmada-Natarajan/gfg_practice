class Solution:
    def maxMeetings(self, s, f):
        
        meetings=[]
        
        for start,finish,idx in zip(s,f,range(1,len(s)+1)):
            
            meetings.append((finish,start,idx))
            
        meetings.sort(key=lambda x:(x[0],x[2]))
        
        ans=[]
        
        last_time=-1
            
        for finish,start,index in meetings:
            if start>last_time:
                ans.append(index)
                last_time=finish
                
        ans.sort()
        return ans
               
            
            
            
            
            
            
            
        