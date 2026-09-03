# Merge Sort

"""
1.Split array in half.
2. Call merge sort on each half to sort them recursively 
3. Merge both sorted halves into one sorted array
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    l = arr[:len(arr)//2]
    r = arr[len(arr)//2:]

    merge_sort(l)
    merge_sort(r)

    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

    return arr


arr = [2, 6, 5, 1, 7, 4, 3]

print(merge_sort(arr))

