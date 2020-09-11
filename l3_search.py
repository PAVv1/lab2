#searching an element
#121910313015_chakrapani  anisetti
#defininig a functin
def search(n, l):
    for i in range( len(l)):
        if l[i] == n:
            return i
#taking an array
l = list(map(int, input("Enter array ").split()))
# input of an element to find
n = int(input("Enter element to find "))
# logicstarts
x = search(n, l)
# output
print("Element ", n, "found at index no.", x)
