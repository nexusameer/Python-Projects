s1 = "abcd"
s2 = "acdb"
count=0
for i in s2:
    for j in s1:
        if i==j:
            count=count+1
            # print(i,j)
            break
# print(count)

if(count==4):
    print("anagrams")
else:
    print("not anagrams")



