a=[1,1,2,3,4,4]
d=[]
for i in a:
    if i not in d:
        d.append(i)
print(d)