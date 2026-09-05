from itertools import combinations

class Solution:
    def powerSet(self, s):
       
        ans=[]
       
        for length in range(len(s)+1):
            for c in combinations(s,length):
                
                ans.append("".join(c))
               
        return ans
       