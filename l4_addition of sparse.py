#addition of sparse matrices
#121910313015_chakrapanianisetti
#defining a function represent Sparse Matrix
# Program to add 2 Sparse Matrices
def sparsematrix(a):
    res = []
    row = len(a)
    col = len(a[0])
    for i in range(row):
        for j in range(col):
            if a[i][j]!=0:
                res.append([i,j,a[i][j]])
    return res

# addition of two sparse matrices
def addition(a1,a2):
    r = []
    l1 = len(a1)
    l2 = len(a2)
    if l1==0 : r = a2
    if l2==0 : r = a1
    i = 0
    j = 0
    while l1>0 and l2>0:
        if a1[i][0]==a2[j][0] and a1[i][1]==a2[j][1]:
            r.append([a1[i][0],a1[i][1],a1[i][2]+a2[j][2]])
            i += 1
            j += 1
        else:
            m = min(a1[i],a2[j])
            r.append(m)
            if m==a1[i]:
                i += 1
            else:
                j += 1
        if i>=l1:
            for x in range(j,l2):
                r.append(a2[x])
            break
        if j>=l2:
            for x in range(i,l1):
                r.append(a1[x])
            break
    return r

# defining Function to print martix
def printmatrix1(a):
    if a==[]: print("EMPTY MATRIX")
    for i in a:
        print(*i)

# defining Function to take input
def input_matrix(r):
    a = [] # Declaring the matrix
    for i in range(r):
        tem = list(map(int,input().split()))
        a.append(tem)
        i += 1
    return a

row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))
print("Enter Martix 1")
a1 = input_matrix(row)
print("Enter Martix 2")
a2 = input_matrix(row)
print("The Original Matrices are")
print("Matrix 1")
printmatrix1(a1)
print("Matrix 2")
printmatrix1(a2)
print()

print("The Sparse Matrices are")
s1 = sparsematrix(a1)
s2 = sparsematrix(a2)
print("Sparse Matrix 1")
printmatrix1(s1)
print("Sparse Matrix 2")
printmatrix1(s2)
print()

print("Addition of 2 Sparse Matrices")
result = addition(s1,s2)
printmatrix1(result)