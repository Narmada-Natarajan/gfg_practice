# Quick Sort

"""
(Divide and Conquer Technique)
Partition

1.Find 



"""

def quicksort(arr):

    if len(arr)<=1:
        return arr

    pivot=arr[-1]
    l=[]
    r=[]

    for x in arr[:-1]:
        if x<=pivot:
            l.append(x)
        else:
            r.append(x)

    return (quicksort(l)+[pivot]+quicksort(r))

arr=[5, 8, 1, 2, 6, 3, 9]
print(quicksort(arr))
