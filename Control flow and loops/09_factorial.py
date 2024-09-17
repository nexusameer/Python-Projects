# find factorial of a number 
n = 5

def Factorial(n):
    if n == 0:
        return True
    else:
        return n*Factorial(n-1)

a=Factorial(10)
print(a)