a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print("The largest number is",a)
elif b>a and b>c:
    print("The largest number is",b)
else:
    print("The largest number is",c)