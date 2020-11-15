string1=input("Enter string ")
s1=[]
f=0
count=0
o="("
c=")"
def checkclose(k):
    if c.index(k)!=o.index(s1[-1]):
        return False
    return True
for i in string1:
    if i in o:
        s1.append(i)
    else:
        if len(s1)==0:
            f=1
            break
        if checkclose(i):
            count+=1
            s1.pop()
if f==1 or len(s1)!=0:
    print("Not safe")
else:
    print(count)