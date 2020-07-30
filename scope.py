# x = 20
# def func1():
#     global x
#     x = 21
#     return x
#
# print(x)
# func1()
# print(x)

x = 89
def rohan():
    x = 20
    def golu():
        global x
        x = 88
    # print("before calling golu()", x)
    golu()
    print("after calling golu()", x)

rohan()
print(x)


