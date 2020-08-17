# Dictionary comprehensions
dict1 = {f"item{i}":i for i in range(100)}
# print(dict1)

# List comprehensions
lst = [i for i in range(10002) if i % 2 == 0]
print(lst)

# Set comprehensions
set1 = {fruit for fruit in ['apple','banana','apple','orange']}
print(set1)
print(type(set1))

# Generator comprehensions
gen1 = (i for i in range(100))
print(gen1.__next__())
