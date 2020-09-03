Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> perfect number
SyntaxError: invalid syntax
>>> n=int(input("enter a number:"))
enter a number:6
>>> count=0
>>> for i in range(1,n):
	if(n%i==0):
		count=count+i

		
>>> if(n==count):
	print("perfect")
else:
	print("not perfect")

	
perfect
>>> 