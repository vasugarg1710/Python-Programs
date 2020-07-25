# Sets in python are data types containing unique elements.
numbers = [1,23,4,32,5] #list
s = set(numbers)
print(type(s))
s.add(23)
s.add(2321)
s.remove(1)
print(s)