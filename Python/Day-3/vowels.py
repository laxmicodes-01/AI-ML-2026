sentence="I Love Python"
vowels="aeiouAEIOU"
a=0
for i in sentence:
    if i in vowels:
        a+=1
print("Number of vowels is:",a)
