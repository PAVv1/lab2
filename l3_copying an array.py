#lab3_copying elements of one array to another
#121910313015_chakrapani anisetti
#initialize an array
arr1=[1,2,3,4,5,6,7,8,9]
#create an array of same length as array 1
arr2=[None] * len(arr1) #len is an inbuilt function
#copying elements from arrray 1 to array 2
#logic starts
for i in range(0 , len(arr1)):
    arr2[i] = arr1[i]
#printing elements of first array
print("elements in array 1 : ")
for i in range (0 , len(arr1)):
    print(arr1[i])
#printing elements in second array
print("elements in array 2: ")
for i in range (0,len(arr2)):
    print(arr2[i])

