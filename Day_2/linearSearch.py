def linear_search(list,num):
    flag=False
    for i in range(0,len(list)):
        if list[i]==num:
            flag=True
            break
    return flag
 
list=[10,20,40,300,56]
n=56
res=linear_search(list,n)
if res==True:
    print("Element Found")
else:
    print("Element Not Found")