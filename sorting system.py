file = input("Enter the text file you want to open: \n")
# open a file for reading and then closes the file
with open(file) as f:
    content = f.read()
    if content == "":
        print("File is empty")
        exit()

# processing with the file
org = content.split()
sort_dict = {}
for index, item in enumerate(org):
    index += 1 # starting index from 1
    sort_dict[str(index) + "."] = item # adding the items with the index to the dictionary


# open the file for appending and closes the file
with open(file, "a") as f:
    f.truncate(0)
    for key, value in sort_dict.items():
        f.write(f"{key} {value} \n") # writing the dictionary in file
print("Sorted items successfully.")
