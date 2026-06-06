a=[1,2,3,1]
d={}
for i in a:
    if i in d:
        print("True")
        break
    d[i]=1
else:
    print("False")
   

