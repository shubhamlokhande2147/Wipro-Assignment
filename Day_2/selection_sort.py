def selection_sort(arr):
    for i in range(0,len(arr)):
        min=arr[i]
        pos=i
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                pos=j
        arr[pos]=arr[i]
        arr[i]=min
    return arr
 
sort_arr=selection_sort([1,6,3,5,7,8])
print(sort_arr)
