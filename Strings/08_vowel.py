a = ['am', ' junior', ' union', ' developer.']
b = 'eiou'
c = []

for word in a:
    for vowel in b:
        if word.startswith(vowel):
            c.append(word)
            break
            

print(c)
