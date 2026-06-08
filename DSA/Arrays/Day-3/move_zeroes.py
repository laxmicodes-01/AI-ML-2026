a=[1,0,2,3,0,4,5]
b=[]
for i in a:
    if i!=0:
        b.append(i)
for i in a:
    if i==0:
        b.append(i)
print(b)