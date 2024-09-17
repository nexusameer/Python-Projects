# n = input("Enter a number: ")
# p = input("Enter a power: ")
# p = int(p)
# n = int(n)
# for i in range(p):
#     if i!=0:
#         n=n*n
        
# print(n)
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
base = float(input("Enter a number: "))
exponent = int(input("Enter a power: "))
print(power(base, exponent))
