# fabnocii_series = 0,1,1,2,3,5,8,13,21,34
n=10
sum=0
prev=0
next = 1
fab=[0,1]
for i in range(n):
    sum=prev+next
    fab.append(sum)
    prev=next
    next=sum

print(fab)
        