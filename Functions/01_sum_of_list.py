l1 = [1,3,5,2,4,66,77,88,99,32]

def sum_list(l1):
    sum =0
    for i in l1:
        sum = sum + i
    return sum
    
print(sum_list(l1))