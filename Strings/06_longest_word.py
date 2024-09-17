a = 'i am a good boy'
l = a.split()
letter = ''
count=0
for i in l:
    if len(i) > count:
        count=len(i)
        letter = i

print(letter)
    
