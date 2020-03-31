lst=[1,2,3,4,3,4,8,10,2,3]
arr=[]
for i in range(len(lst)):
    if lst[i] not in arr:
        arr.append (lst[i])
    else:
        arr.append ("N")
print(arr)
