#linkedlist_2
#121910313015_chakrapanianisetti
#define a class
class Node:
    #defining a function
    def insnode(self,data=None,next=None):
        self.data =data
        self.next= next

#definig a function to insert nodes
def insert(amp, item):
    temp=Node()
    temp.data=item
    temp.Next=amp
    amp=temp
    return amp

#defining a function to display
def display(amp):
    while(amp!=None):
        print(amp.data,end =" ")
        amp=amp.Next
#defining a function to create a linked list
def createlist1(arr,n):
    amp=None
    for i in range(n-1,-1,-1):
        amp=insert(amp,arr[i])
    return amp

arr=[1,2,3,4,5]
n=len(arr)
amp=createlist1(arr,n)
display(amp)