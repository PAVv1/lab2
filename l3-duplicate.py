#program to remove duplicate elements in an array
#121910313015_chakrapani anisetti
#initialize an array
arr=[8,1,7,9,4,8,9,8,7,2]
#crete another array with no elements in it
arr1=[]
#logic starts
for i in arr :
    if i not in arr1:
        arr1.append(i)

print(arr1)
