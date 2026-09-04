class Solution:
    def nextPermutation(self, arr):

        n = len(arr)
        if n <= 1:
            return arr

        # Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1

        # If pivot is found, find the successor and swap
        if i >= 0:
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]

        # Reverse the elements after the pivot index
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

        