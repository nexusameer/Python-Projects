a = 'abcaeidjl'
b = 'aeiou'
c = a
for i in a:
    for j in b:
        if i == j:
            c = c.replace(i,'')
    
print(c)