n=int(input("enter the number of lines"))

c = n-1
for i in range(1,n+1):
    print(" "*c,end= "")

    print("* "*i)
    c -= 1
