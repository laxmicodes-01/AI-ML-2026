a=input("Enter string:")
vowels=0
for i in a:
    if i in "aeiouAEIOU":
        vowels=vowels+1
        print("The number of vowels in string is",vowels)