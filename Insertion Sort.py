# Insertion Sort

"""
1. Take the current element -->key
2. Compare it with elements on the left
3. Shift bigger one position right
4. Insert key in the correct position

"""

arr=[5,3,8,4,2]

n=len(arr)

for i in range(1,n):
    k=arr[i]
    j=i-1

    while j>=0 and k<arr[j]:
        arr[j+1]=arr[j]
        j-=1   

    arr[j+1]=k

print(arr)

