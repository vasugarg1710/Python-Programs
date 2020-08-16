# def gen(num):
#     for i in range(num):
#         yield i
# print(gen(3))
def gen_factorial(fac):
    for i in range(1,fac):
        fac = fac * i
    yield fac
print(gen_factorial(5).__next__())

#Generator Comprehension
gen2 = (i for i in range(100) if i%2==0)
print(gen2.__next__())
print(gen2.__next__())

for i in gen2:
    print(gen2.__next__())
