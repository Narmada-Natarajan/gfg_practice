import heapq

class Solution:
    def minAnd2ndMin(self, arr):
        
        s=set(arr)
        if len(s)<2:
            return[-1]
        return heapq.nsmallest(2,s)
        
        
