#armstrong number
n=int(input("enter a number:"))
sum=0
pre=n
while(pre>0):
        res = pre % 10
        sum = sum+res*res*res
        pre =pre//10

if(n==sum):
    print("armstrong number")
else:
    print("not armstrong number")