def weights(arr):
    for i in range(0,len(arr)):
        min=arr[i]
        pos=i
        for j in range(i+1,len(arr)):
            if arr[j]> min:
                min=arr[j]
                pos=j
        arr[pos]=arr[i]
        arr[i]=min
    return arr
 
sort_arr= weights([95.7,59.6,91.0,84.9,76.2,65.3,95.4])
print(sort_arr)
