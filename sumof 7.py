lst=[]
t1=(4,5)
t2=(6,1)
t3=(3,6)
t4=(4,3)
t5=(2,5)

lst.append(t1)
lst.append(t2)
lst.append(t3)
lst.append(t4)
lst.append(t5)

print(lst)
for i in (lst):
    if sum(i)==7:
        print(i)
    else:
        print("not equal to 7")
    
