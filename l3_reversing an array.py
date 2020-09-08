#printing elements in an array in reverse order
#121910313015_chakrapani anisetti
#initialize an array
arr1=[1,3,5,7,4]
#printing elements in first array
print("elements in array 1: ")
for i in range(0,len(arr1)):
    print(arr1[i])
#to print elements of array1 in reverse order in array 2
print("elements in array 1 in reverse order:")
for i in range(len(arr1)-1,-1,-1):
    print(arr1[i])
