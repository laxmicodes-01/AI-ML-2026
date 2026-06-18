stack="Hello"
print(stack[::-1])


s=[1,2,3,4]
s.reverse()
print(s)

s="HELLO"
a=[]
for i in s:
    a.append(i)

rev=""
while a:
    rev+=a.pop()
print(rev)