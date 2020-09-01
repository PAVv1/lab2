a=int(input("enter first number:"))
b=int(input("enter second number:"))
if(x > y):
  great=x
else:
   great=y
while(true):
  if((great%a==0) and (great %y ==0)):
    lcm=great
      break
    great+=1
print("lcm is:"+lcm)
