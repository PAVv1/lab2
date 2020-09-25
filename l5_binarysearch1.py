#binarysearch
#121910313015_chakrapani anisetti
#defining an array
arr=[1,2,3,4,5,6,7,8]
count=0
target=int(input("enter a value to search:"))
low=int(input("enter low limit:"))
high=len(arr)
while high>=0:
    i=(low+high)//2
    if arr[i]==target:
        count=count+1
        break
    elif arr[i]>target:
        high=i-1
    else:
        low=i+1
if(count!=0):
    print("element is found at:",i)
else:
    print("element is not found")