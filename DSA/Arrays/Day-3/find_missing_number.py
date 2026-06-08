a=[1,2,5]

a.sort()
b=a[-1]
for i in range(b+1):
    if i not in a:
        print(i)