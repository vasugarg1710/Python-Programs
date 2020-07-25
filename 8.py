# Faulty calculator
print("Enter the operator:\n+\n-\n*\n/")
operator = input()
print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
if (operator=="+"):
    if (a==56 and b==9):
        print(77)
    else:
        print(a+b)
elif (operator=="-"):
    print(a-b)
elif (operator=="*"):
    if (a==45 and b==3):
        print(555)
    else:
        print(a*b)
elif (operator=="/"):
    if (a==56 and b==6):
        print(4)
    else:
        print(a/b)
else:
    print("invalid operator")