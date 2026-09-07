class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        
        work=[]
        
        for s,f in zip(start,finish):
            
            work.append((f,s))
            
        work.sort(key=lambda x: x[0])
        
        count=0
        finish_time=-1
        
        for finish,start in work:
            if start>finish_time:
                count+=1
                finish_time=finish
            
        return count
            
        