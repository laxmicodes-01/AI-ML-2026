fruits={"name":"Strawberry","quantity":10}
fruits["quantity"]=20
print(fruits)
for i in fruits.keys():
    print(i)
for i in fruits.values():
    print(i)
for i, j in fruits.items():
    print(i, j)