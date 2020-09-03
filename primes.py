#primenumbers
a=int(input("enter lower limit:"))
b=int(input("enter upper limit:"))
for i in range(a,b):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i)







