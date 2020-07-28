"""
File IO basics
r - for reading a file
w - for writing in a file
x - create a file if not exist
a - adds more content to a file
t - text mode
b - binary mode
"""

f = open("bhai.txt","w")
# print(f.read())

# while True:
#     f.write("Bhai kaise ho\n")
#     for line in f:
#         print(line)
# f.close()

list = ['apple','banana','orange','hello','vasu','kya chal raha hai','zindagi']
for n in range(0,len(list)):
    f.write("Bhai Kaise ho ")
    f.write(list[n])
    f.write("\n")
