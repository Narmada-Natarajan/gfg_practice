#BUBBLE SORT

"""
1. Compare adjacent elements , if l>r-->swap
2. Largest element is pushed to the end
3. n-i-1 because last i is already sorted

"""

arr=[5,1,3,2,4]

n=len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)


