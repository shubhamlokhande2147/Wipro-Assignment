def binary_search(list,num):
    flag=False
    #index pos of starting element in list
    low=0
    #index pos of last element in list
    high=len(list)-1
    mid=0
    while(low<=high):
        #middle element pos
        mid=(low+high)//2
        #if search element is greater than middle
        if  num>list[mid]:
            low=mid+1
        elif num<list[mid]:
            high=mid-1
        else:
            flag=True
            break
    return flag
