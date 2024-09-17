def EvOd(n):
    if n>0:
        if n%2 == 0:
            return 'Even'
        else:
            return 'Odd'
    elif n<0:
        return 'Negative Number'
    else:
        return 'Zero'
    
print(EvOd(101))
