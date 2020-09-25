#linear_search using userdefined function
#121910313015_chakrapani anisetti
#defining a function
def linear_search(arr1,l,target):
    for i in range(len(arr1)):
        if arr1[i]== target:
            return i
    return -1
arr=[1,2,3,4,5,6,7]
target=7
l=len(arr)
result=linear_search(arr,len(arr),7)
if(result==-1):
    print("element is not found")
else:
    print("element is found at index:",result)