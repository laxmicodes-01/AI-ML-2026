s = input("Enter parentheses: ")

stack = []

for ch in s:

    if ch == '(':
        stack.append(ch)

    elif ch == ')':

        if len(stack) == 0:
            print("Not Balanced")
            break

        stack.pop()

else:

    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")