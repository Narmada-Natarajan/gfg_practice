class Solution:    
    def rotateDeque(self, dq, type, k):
        
        if type==1:
            for i in range(k):
                dq.appendleft(dq.pop())
            
        else:
            for i in range(k):
                dq.append(dq.popleft())
        
