# If else
print("What is your age")
age = int(input())
if (age<5 or age>100):
    print("Invalid age")
elif (age<18):
    print("You cannot drive")
elif (age>18):
    print("You can drive")
else:
    print("We cannot decide")