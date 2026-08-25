import math
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        
        arr.sort()

        floor = -1
        ceil = -1

        for num in arr:
            if num <= x:
                floor = num
            if num >= x:
                ceil = num
                break

        return [floor, ceil]
        