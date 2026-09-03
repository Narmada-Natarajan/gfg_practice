# Selection Sort

"""
1. Assume i is minimum.
2. Search remaining array for a smaller element.
3. Swap the min with arr[i]

"""
arr=[24,41,33,42,17]

n=len(arr)

for i in range(n-1):
    mini=i #0 idx as min , 4 (pass1) | pass2 mini=1idx

    for j in range(i+1,n): #j --> 1 to 4
        if arr[j]<arr[mini]: #41<24? No , 33<24? No ,42<24? No , 17<24? Yes 
            mini=j #mini=4(idx)
            arr[i],arr[mini]=arr[mini],arr[i]
            #24,17=17,24
print(arr)





        
