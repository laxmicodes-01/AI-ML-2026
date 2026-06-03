a=[2,5,8,9,6,3]
max=a[0]
second_max=a[0]
for i in a:
    if i>=max:
        second_max=max
        max=i
    elif i>=second_max and i!=max:
        secondmax=i
print(second_max)
