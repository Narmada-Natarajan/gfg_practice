class Solution:
    def longestCommonPrefix(self, arr):
        
        ans=""
        
        for i in range(len(arr[0])):
            ch=arr[0][i]
            for word in arr:
                if i>=len(word) or word[i]!=ch:
                    return ans
            ans+=ch
            
        return ans
        
        
        