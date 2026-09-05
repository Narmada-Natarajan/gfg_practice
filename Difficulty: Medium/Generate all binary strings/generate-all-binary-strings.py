class Solution:
    def binstr(self, n):
        
        binary=[(bin(i)[2:]).zfill(n) for i in range(2**n)]
        
        return binary
        