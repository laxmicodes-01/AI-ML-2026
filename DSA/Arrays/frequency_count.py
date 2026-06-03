a=[1,1,55,6,2,44,8]
map={}
for i in a:
    if i in map:
        map[i]+=1
    else:
        map[i]=1
print(map)