# Twin primes upto a specified limit

# input
n = int(input("Enter limit : "))
# using isPrime function
def IsPrime(k: int):
    flag = 0
    for i in range(2, int((k / 2) + 1)):
        if (k % i) == 0:
            flag = 1
            break
    if flag == 1:
        return False
    else:
        return True


for i in range(2, n):
    if i + 2 < n:
        if (IsPrime(i) == True) and (IsPrime(i + 2) == True):  # checking two numbers are prime are not
            print("(", i, " ,", i + 2, ")")

