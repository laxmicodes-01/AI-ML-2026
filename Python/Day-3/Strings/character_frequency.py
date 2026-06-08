a="banana"
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
b=d.values()
print(max(b))
print([key for key, value in d.items() if value == max(b)])