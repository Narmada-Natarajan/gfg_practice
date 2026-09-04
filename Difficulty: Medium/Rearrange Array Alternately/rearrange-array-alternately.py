class Solution:
    def rearrange(self, arr):
        
        n = len(arr)
        if n <= 1:
            return arr

        # sort the array to make sure min/max pointers work correctly
        arr.sort()

        maxi = n - 1
        mini = 0

        #Find the static maximum element AFTER sorting
        maxe = arr[n - 1] + 1 

        # Apply the mathematical encoding trick
        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[maxi] % maxe) * maxe
                maxi -= 1
            else:
                arr[i] += (arr[mini] % maxe) * maxe
                mini += 1 

        # Decode the values back in-place
        for i in range(n):
            arr[i] //= maxe

        return arr
