def IncreFun(n):
    return 5 + (n == 2) * 2

n = int(input('Enter a Number='))
print(IncreFun(n))