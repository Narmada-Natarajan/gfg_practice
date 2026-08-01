import numpy as np 

class Solution:
    def rotateMatrix(self, mat):
        
        mat[:]=[list(row) for row in zip(*mat)]
        mat.reverse()        
        return mat
        