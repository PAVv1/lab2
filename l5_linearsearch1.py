#linear_search
#121910313015_chakrapani anisetti
#defining an array
arr=[1,2,3,4,5,6,7]
target=int(input("enter an element to search :"))
count=0
l=len(arr)
for i in range(l):
    if arr[i]==target:
        count=count+1
        break

if(count!=0):
    print("element is found at index",i)
else:
    print("element is not found")
