arr=[1,1,1,2,2,3,4,5]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)