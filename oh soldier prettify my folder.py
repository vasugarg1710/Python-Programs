import os


def soldier(path, file, format):
    files = os.listdir(path)
    os.chdir(path)
    with open(file) as f:
        content = f.read()
        # print(content)
    i = 0

    for item in files:
        if item not in content:
            if item.endswith(format):
                i = i + 1
                os.rename(item, str(i) + format)
                files.remove(item)
            else:
                name = item.capitalize()
                os.rename(item, name)


if __name__ == '__main__':
    path = input("Enter the path of the folder which you want to prettify: \n")
    file = input("Enter the text file in which the excluding files are written (eg. exclude.txt): \n")
    format = input("Enter the file format you want to sort with 1,2,3.... (eg .jpg) \n")
    soldier(path, file, format)
    print("Folder prettified")
