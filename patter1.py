n=int(input("enter the number of levels"))
a=(3*n)+2
for i in range(1,a+1):
    if i%3==0:
        print("****")
    else:
        print("*  *")
