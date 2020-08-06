def funcprint(*args):
    """This function prints all the items in a list"""
    for item in args:
        print(item)


lst = ["Rohan", "Tanay", "Dhruv", "Ayushman", "Vedansh"]
funcprint(*lst)
